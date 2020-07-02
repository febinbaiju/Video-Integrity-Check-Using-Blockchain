from tinyec import registry

privKey = int("40884892330116115743588172330864273153245470794831389841717904431882180525464")
curve = registry.get_curve('brainpoolP256r1')
g = curve.g

def compute_public_ciphertext():
    ciphertextPubKey = 1 * g
    return (ciphertextPubKey)

(ciphertextPubKey) = compute_public_ciphertext()

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def ecc_calc_decryption_key(privKey, ciphertextPubKey):
    sharedECCKey = ciphertextPubKey * privKey
    return sharedECCKey

decryptKey = ecc_calc_decryption_key(privKey, ciphertextPubKey)
print("DECRYPTION KEY:", compress_point(decryptKey))