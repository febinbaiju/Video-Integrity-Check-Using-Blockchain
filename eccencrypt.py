from tinyec import registry
import secrets

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def ecc_calc_encryption_keys(pubKey, curve):
    ciphertextPubKey = 1 * curve.g
    sharedECCKey = pubKey * 1
    return (sharedECCKey, ciphertextPubKey)

def ecc_calc_decryption_key(privKey, ciphertextPubKey):
    sharedECCKey = ciphertextPubKey * privKey
    return sharedECCKey

def get_encrypted_key():
    curve = registry.get_curve('brainpoolP256r1')
    privKey = secrets.randbelow(curve.field.n)
    g = curve.g
    pubKey = privKey * g

    (encryptKey, ciphertextPubKey) = ecc_calc_encryption_keys(pubKey, curve)
    return (privKey, compress_point(encryptKey))
