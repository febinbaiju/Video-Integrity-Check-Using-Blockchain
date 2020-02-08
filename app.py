import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org

# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]
# Greeter contract ABI
abi = json.loads('[{"constant":false,"inputs":[{"internalType":"string","name":"_filename","type":"string"},{"internalType":"string","name":"_filepath","type":"string"}],"name":"createFileEntry","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"fileCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getLastEntry","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
# Greeter contract address - convert to checksum address
address = web3.toChecksumAddress('0x33B5dDA0Dd5625a230512f800f3a88b4c92de192') # FILL ME IN
# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)

# Read the default greeting
print(contract.functions.getLastEntry().call())
# Set a new greeting

tx_hash = contract.functions.createFileEntry('newfilenameTest','newfilepathTest').transact()
# Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)
# Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.getLastEntry().call()
))
