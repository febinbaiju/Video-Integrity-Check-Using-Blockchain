from tinyec import registry
import secrets

curve = registry.get_curve('brainpoolP256r1')

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def ecc_calc_encryption_keys(pubKey):
    ciphertextPubKey = 1 * curve.g
    sharedECCKey = pubKey * 1
    return (sharedECCKey, ciphertextPubKey)

def ecc_calc_decryption_key(privKey, ciphertextPubKey):
    sharedECCKey = ciphertextPubKey * privKey
    return sharedECCKey

privKey = secrets.randbelow(curve.field.n)
g = curve.g
pubKey = privKey * g

(encryptKey, ciphertextPubKey) = ecc_calc_encryption_keys(pubKey)
print("share this key: ",privKey)
print("ENCRYPTION KEY:", compress_point(encryptKey))