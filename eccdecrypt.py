from tinyec import registry



def compute_public_ciphertext(g):
    ciphertextPubKey = 1 * g
    return (ciphertextPubKey)

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def ecc_calc_decryption_key(privKey, ciphertextPubKey):
    sharedECCKey = ciphertextPubKey * privKey
    return sharedECCKey

def decrypt_key(pkey):
    privKey = int(pkey)
    curve = registry.get_curve('brainpoolP256r1')
    g = curve.g
    (ciphertextPubKey) = compute_public_ciphertext(g)
    decryptKey = ecc_calc_decryption_key(privKey, ciphertextPubKey)
    return compress_point(decryptKey)
