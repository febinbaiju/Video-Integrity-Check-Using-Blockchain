import hmac
import hashlib
from Settings import *

def hmacsha_file(filename,key):
    digest_maker = hmac.new(bytes(key,'utf-8'),b'',hashlib.sha256,)
    with open(filename, 'rb') as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    digest = digest_maker.hexdigest()
    return digest

def hmacsha(string,key):
    h = hmac.new( bytes(key,'utf-8'),bytes(string, 'utf-8') , hashlib.sha256 )
    return h.hexdigest()