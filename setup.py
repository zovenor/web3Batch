import setuptools

with open('README.md', 'r', encoding='utf8') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="web3Batch",
    version="0.0.1",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
