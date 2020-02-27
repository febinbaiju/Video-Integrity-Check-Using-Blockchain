
# Python program to find SHA256 hash string of a file
import hashlib
 
def sha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

print(sha256('output.avi'))
#print(sha256('output001.mp4'))