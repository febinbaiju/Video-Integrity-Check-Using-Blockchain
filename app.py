import json
from web3 import Web3
from eccdecrypt import decrypt_key
from Settings import *

class Blockchain():
    def __init__(self):
        self.contract = None
        self.web3 = None
        self.connect()

    def connect(self):
        # Set up web3 connection with Ganache
        ganache_url = GANACHE_URL
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        # TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org
        # Set a default ac. hem count to sign transactions - this account is unlocked with Ganache
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        
        # Greeter contract ABI
        f = open("abi_blockchain_Files_Contract.json","r")
        abi = json.loads(f.read())
        
        # Greeter contract address - convert to checksum address
        address = self.web3.toChecksumAddress(CONTRACT_ADDRESS) # FILL ME IN
        
        # Initialize contract
        self.contract = self.web3.eth.contract(address=address, abi=abi)


    def add(self,_filename,_filepath,_pubkey,_filehash):
        # Read the default greeting
        tx_hash = self.contract.functions.createFileEntry(_filename,_filepath,str(_pubkey),_filehash).transact()
        # Wait for transaction to be mined
        self.web3.eth.waitForTransactionReceipt(tx_hash)
        
        print(self.contract.functions.getLastEntry().call())
        print(self.contract.functions.getTotalCount().call())

    def getKeys(self):
        keys = []
        for key in self.contract.functions.getKeys().call():
            if key!="":
                keys.append(decrypt_key(key))
        return keys

    def getHashes(self):
        hashes = []
        for hash in self.contract.functions.getHashes().call():
            if hash!="":
                hashes.append(hash)
        return hashes