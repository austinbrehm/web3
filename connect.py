"""Connect to Infura and access Ethereum blockchain data.

This module is meant to be executed as a script. It will retrieve
an Infura API key, connect to Infura, and retrieve blockchain data.

Usage:
    python connect.py
    python connect.py --ens austin.eth

Options:
    -h, --help      Show the help menu.
    --ens           Show data for a specific Ethereum Name Service (ENS) name.
"""

import argparse
import subprocess

import web3
import colorama


def get_infura_key() -> str:
    """Get the Infura API key from .bashrc file.

    Returns:
        key: Infura API key, stored in .bashrc file.
    """
    key = subprocess.run(
        "source ~/.bashrc && echo $INFURA_KEY",
        shell=True,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.rstrip()

    return key


if __name__ == "__main__":
    # Create argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument("--ens", help="Get address of ENS name")
    args = parser.parse_args()

    # Initalize color for CLI.
    colorama.init(autoreset=True)

    # Get Infura API key.
    api_key = get_infura_key()

    # Connect to Infura via HTTP.
    provider = web3.Web3(
        web3.Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{api_key}")
    )

    if provider.is_connected():
        print(colorama.Fore.GREEN + "\nEthereum Blockchain Data 📊")

        # Get most recent block number.
        print(f"🧊 Latest Proposed Block Number: {provider.eth.get_block_number()}")

        # Get current gas price.
        print(
            f"⛽️ Current Gas Price: {round(provider.eth.gas_price * 10E-10, 3)} gwei\n"
        )

        if args.ens:
            # Get account information for ENS name.
            print(colorama.Fore.BLUE + "Ethereum Name Service (ENS) Data 🪪")
            address = provider.ens.address(args.ens)
            balance = round(provider.eth.get_balance(address) * 10e-19, 5)  # in ETH
            txs = provider.eth.get_transaction_count(address)
            print(f"🆔 ENS Name: {args.ens}")
            print(f"🏠 Ethereum Address: {address}")
            print(f"💸 ETH Balance: {balance} eth")
            print(f"✉️ Total Transactions: {txs}\n")
    else:
        print(
            colorama.Fore.RED
            + "❌ Unable to connect to Infura. Make sure API key is up to date."
        )
