import hmac
import hashlib

def hmacsha(filename):
    digest_maker = hmac.new(b'video_secret_key',b'',hashlib.sha256,)
    with open(filename, 'rb') as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    digest = digest_maker.hexdigest()
    return digest
