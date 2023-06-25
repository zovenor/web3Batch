# web3Batch.py

### Installation
```commandline
pip install web3Batch
```
### Example

```python
from web3 import Web3
from web3Batch import We3Batch

contract_addresses = ['0x...', '0x...', ...]
endpoint_uri = 'https://localhost:6000'

web3 = Web3(Web3.HTTPProvider(endpoint_uri))

# Your abi for contracts
abi = {...}

contracts = [web3.eth.contract(
    address=web3.to_checksum_address(contract_address)
) for contract_address in contract_addresses]

wb = Web3Batch(endpoint_uri)

for contract in contracts:
    wb.add_contract_request(
        contract=contract,
        fn_name='balanceOf',
        args=(web3.to_checksum_address(contract.address))
    )

responses = wb.send_requests()
```
