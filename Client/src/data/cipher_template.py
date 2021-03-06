try:
	import os
	import sys
	import traceback
	# Import directives here

except Exception as e:
	return 10, [e, traceback.format_exc()]

class IdleCipher(object):

    def __init__(self):
        pass

    def get_info(self):
        information = {
        "name": "Cipher Name",
        # Type can be the following:
        # encryption: Encrypting messages
        # signature: Signing messages
        # hash: hashing data
        "type": "encryption,signature,hash",
        "description": "Cipher description",
        "encryption_values": {"key": "str", "plaintext": "str"},
        "decryption_values": {"key": "str", "ciphertext": "str:bytes"}
        }

        return information

    def encrypt(self, key, plaintext):
    	return key + plaintext[::-1] + key

    def decrypt(self, key, ciphertext):
        return ciphertext.replace(key, "")[::1]

    def sign(self, key, data):
        # For signature cipher algorithms only
        return data + key

    def verify(self, key, data):
        # For signature cipher algorithms only
        if key in data:
            return True

        else:
            return False

    def hash(self, data):
        # For hashing algorithms only
        return data
