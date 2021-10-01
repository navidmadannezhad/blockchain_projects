from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import numpy as np

from . import digital_signature
from .block import Block

class Transaction:
    inputs = None
    outputs = None
    sig = None
    public_key = None

    def __init__(self, public_key):
        self.public_key = public_key
        self.inputs = []
        self.outputs = []
        
    def add_input(self, from_address, amount):
        input = {'from_address': from_address, 'amount': amount}
        self.inputs.append(input)

    def add_output(self, to_address, amount):
        output = {'to_address': to_address, 'amount': amount}
        self.outputs.append(output)

    def signTransactionWith(self, private_key):
        message = self.__gather()
        self.sig = digital_signature.sign(message=message, privateKey=private_key)

    def __gather(self):
        data = np.array([self.inputs, self.outputs])
        return data.tobytes()


    def is_valid(self):
        message = self.__gather()
        # here we got problem
        if digital_signature.verify(message, self.sig, self.public_key):

            input_amount_sum = 0
            for _input in self.inputs:
                input_amount_sum = input_amount_sum + _input['amount']     
            output_amount_sum = 0
            for _output in self.outputs:
                output_amount_sum = output_amount_sum + _output['amount'] 
            if output_amount_sum <= input_amount_sum:
                return True
            else:
                return False

        else:
            return False

    def __repr__(self):
        return 'inputs are {}\n'.format(self.inputs)+' and outputs are {}\n'.format(self.outputs)+' and transaction is {}'.format(self.is_valid() and 'Valid' or 'InValid')


# class TransactionBlock(Block):




















































# class walletAccount:
#     private_key = None
#     public_key = None
#     account_number = None

#     def __init__(self, account_number):
#         self.private_key =  rsa.generate_private_key(public_exponent=65537, key_size=2048)
#         self.public_key = self.private_key.public_key()
#         self.account_number = account_number

#     def __repr__(self):
#         return 'Account Number: {}\n'.format(self.account_number)+'Public Key: {}\n'.format(self.public_key)+'Private Key: {}\n'.format(self.private_key)






    