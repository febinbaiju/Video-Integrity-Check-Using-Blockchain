import json
from web3 import Web3
import hmac
import hashlib


class Blockchain():
    def __init__(self):
        self.contract = None
        self.web3 = None
        self.connect()

    def connect(self):
        # Set up web3 connection with Ganache
        ganache_url = "http://127.0.0.1:7545"
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        # TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org
        # Set a default account to sign transactions - this account is unlocked with Ganache
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        
        # Greeter contract ABI
        abi = json.loads('[{"constant":false,"inputs":[{"internalType":"string","name":"_filename","type":"string"},{"internalType":"string","name":"_filepath","type":"string"},{"internalType":"string","name":"_filehash","type":"string"}],"name":"createFileEntry","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"fileCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getLastEntry","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getTotalCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
        
        # Greeter contract address - convert to checksum address
        address = self.web3.toChecksumAddress('0x90F162990f3100d881Af4835B6CbD3cbed0F245f') # FILL ME IN
        
        # Initialize contract
        self.contract = self.web3.eth.contract(address=address, abi=abi)

    def add(self,_filename,_filepath,_filehash):
        # Read the default greeting
        print(self.contract.functions.getLastEntry().call())
        
        tx_hash = self.contract.functions.createFileEntry(_filename,_filepath,_filehash).transact()
        # Wait for transaction to be mined
        self.web3.eth.waitForTransactionReceipt(tx_hash)
        
        print(self.contract.functions.getLastEntry().call())
        print(self.contract.functions.getTotalCount().call())