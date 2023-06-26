from typing import (
    List,
    Tuple,
    Any,
    Dict,
    Optional,
    Union
)

import httpx
import aiohttp
from eth_typing import URI
from web3.contract import Contract

from .types import Payload


class Web3Batch:
    endpoint_uri: Optional[Union[URI, str]]
    payloads: List[Payload]

    def __init__(self, endpoint_uri: Optional[Union[URI, str]]) -> None:
        self.endpoint_uri = endpoint_uri
        self.payloads = []

    @staticmethod
    def _get_payload_with_contract(
            _id: int,
            contract: Contract,
            fn_name: str,
            args: Optional[Tuple[Any]] = None,
            kwargs: Optional[Dict[str, Any]] = None) -> Payload:
        _data = contract.encodeABI(fn_name=fn_name, args=args, kwargs=kwargs)
        payload = Payload(
            {
                'id': _id,
                'jsonrpc': '2.0',
                'method': 'eth_call',
                'params': [
                    {
                        'to': contract.address,
                        'data': _data
                    }
                    , 'latest']
            }
        )
        return payload

    def add_contract_request(
            self,
            contract: Contract,
            fn_name: str,
            args: Optional[Tuple[Any]] = None,
            kwargs: Optional[Dict[str, Any]] = None
    ) -> None:
        _id = len(self.payloads) + 1
        payload = self._get_payload_with_contract(
            _id=_id,
            contract=contract,
            fn_name=fn_name,
            args=args,
            kwargs=kwargs
        )
        self.payloads.append(payload)

    def clear_requests(self):
        self.payloads.clear()

    def send_requests(self, headers=None) -> List[Dict]:
        if not headers:
            headers = {}

        with httpx.post(self.endpoint_uri, json=self.payloads, headers=headers) as response:
            assert response.status_code != 200, f'Status code: {response.status_code}!'

            response_json = response.json()
            response_json.sort(key=lambda obj_response: obj_response['id'])
            return response_json

    async def send_requests_async(self, headers=None) -> List[Dict]:
        if not headers:
            headers = {}

        async with aiohttp.ClientSession() as session:
            async with session.post(self.endpoint_uri, json=self.payloads, headers=headers) as response:
                response_json = await response.json()
                response_json.sort(key=lambda obj_response: obj_response['id'])
                return response_json
