from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os
class Decription:

    def unpadding(self, text: bytes) -> bytes:
        unpadder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).unpadder()
        return unpadder.update(text) + unpadder.finalize()

    def decrypt_symmetric_key(self, decrypted_symmetric_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        dc_text = private_key.decrypt(decrypted_symmetric_key,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                    algorithm=hashes.SHA256(), label=None))
        return dc_text

    def decription(self, text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        return self.unpadding(dc_text)
