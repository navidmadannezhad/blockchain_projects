from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import numpy as np

class Transaction:
    inputs = None
    outputs = None
    sig = None

    def __init__(self):
        self.inputs = []
        self.outputs = []
        
    def add_input(self, from_address, amount):
        input = [from_address, amount]
        self.inputs.append(input)

    def add_output(self, to_address, amount):
        output = [to_address, amount]
        self.outputs.append(output)

    def signTransactionWith(self, private_key):
        message = self.__gather()
        self.sig = private_key.sign(message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

    def __gather(self):
        data = np.array([self.inputs, self.outputs])
        return data.tobytes()


    def transactionIsValid(self):
        pass

    def __repr__(self):
        return 'inputs are {}\n'.format(self.inputs)+' and outputs are {}\n'.format(self.outputs)+' and the signature is {}\n'.format(self.sig)


class walletAccount:
    private_key = None
    public_key = None
    account_number = None

    def __init__(self, account_number):
        self.private_key =  rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()
        self.account_number = account_number

    def __repr__(self):
        return 'Account Number: {}\n'.format(self.account_number)+'Public Key: {}\n'.format(self.public_key)+'Private Key: {}\n'.format(self.private_key)

    


account1 = walletAccount(1)
account2 = walletAccount(2)
account3 = walletAccount(3)

tx2 = Transaction()
tx2.add_input(account1.public_key, 250)
tx2.add_output(account3.public_key, 250)
tx2.signTransactionWith(account2.private_key)

print(tx2)





    