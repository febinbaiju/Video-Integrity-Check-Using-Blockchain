import hmac
import hashlib
from Settings import *

def hmacsha_file(filename):
    digest_maker = hmac.new(bytes(Video_Secret_Key,'utf-8'),b'',hashlib.sha256,)
    with open(filename, 'rb') as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    digest = digest_maker.hexdigest()
    return digest

def hmacsha(string):
    h = hmac.new( bytes(String_Secret_Key,'utf-8'),bytes(string, 'utf-8') , hashlib.sha256 )
    return h.hexdigest()
