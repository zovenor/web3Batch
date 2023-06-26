import setuptools

with open('README.md', 'r', encoding='utf8') as readme_file:
    long_description = readme_file.read()

version = '0.0.3'

setuptools.setup(
    name="web3Batch",
    version=version,
    author="zovenor",
    author_email="zovenor@gmail.com",
    description="Library to send batch requests using web3.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zovenor/web3Batch",
    project_urls={
        "Bug Tracker": "https://github.com/zovenor/web3Batch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['web3Batch'],
    python_requires=">=3.6",
    install_requires=['aiohttp', 'web3', 'httpx']
)
