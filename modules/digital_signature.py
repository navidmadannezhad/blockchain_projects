from cryptography.hazmat import primitives
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key

import cryptography.hazmat.primitives.asymmetric.rsa as rsaAlgorithm
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature


def generate_keys():
    privateKey = rsaAlgorithm.generate_private_key(
        backend=None,
        key_size=2048,
        public_exponent=65537
    )
    publicKey = privateKey.public_key()

    # returns objects of keys
    return privateKey, pu_to_pem(publicKey)


def pu_to_pem(pu):
    pem_pu = pu.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem_pu

def pr_to_pem(pr):
    pem_pr = pr.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem_pr

def pem_to_pr_obj(pem_pr):
    private_key = serialization.load_pem_private_key(
        pem_pr,
        password=None,
    )
    return private_key

def sign(message, privateKey):
    signature = privateKey.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature




def verify(message, signature, publicKey):
    publicKey_instance = serialization.load_pem_public_key(
        publicKey,
    )

    try:
        publicKey_instance.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
        
    except InvalidSignature:
        return False


if __name__ == '__main__':

# Clinet base
    publicKey, privateKey = generate_keys()
    message = b'Hello navid! from cryptography!'
    signature = sign(message, privateKey)

# Attacker base
    message = b'Fuck u navid! from cryptography!'

    try:
        verify(message, signature, publicKey)
        print('Authenticated!')
    except InvalidSignature:
        print('not authenticated! some issues have been occured!')