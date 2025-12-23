"""
Connect to a provider for the Ethereum blockchain.
"""

import subprocess

from web3 import Web3, EthereumTesterProvider


def get_infura_key() -> str:
    """Get the Infura API key from bashrc file.

    Returns:
        key: Infura API key, stored in .bashrc file.
    """
    subprocess.run("source ~/.bashrc", shell=True)
    key = subprocess.run(
        "echo $INFURA_KEY", shell=True, capture_output=True, text=True
    ).stdout.rstrip()

    return key


# Connect to a test provider.
# provider = Web3(EthereumTesterProvider())
# latest_block = provider.eth.get_block("latest")
# print(latest_block.timestamp)


if __name__ == "__main__":
    print(get_infura_key())
