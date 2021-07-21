from cryptography.hazmat import primitives
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key


import cryptography.hazmat.primitives.asymmetric.rsa as rsaAlgorithm
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

def generate_keys():
    privateKey = rsaAlgorithm.generate_private_key(
        backend=None,
        key_size=2048,
        public_exponent=65537
    )
    publicKey = privateKey.public_key()

    return publicKey, privateKey



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
    publicKey.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


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