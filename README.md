# eth-connect
Retrieve data from the Ethereum blockchain. 

## Setup
### Infura
1. Create an [Infura](https://www.infura.io/) account
2. Within the MetaMask Developer Portal, create an API key

### Git Bash
1. From the home directory, open .bashrc file
2. Type the following, replacing "abc123" with API key from Infura: 
`
export INFURA_KEY="abc123"
` 

## Usage
Run the connect.py script:
`
python connect.py
`

OR

Run the connect.py script with optional arguments:
`
python connect.py --ens <insert domain name>
`