from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os
class Encryption:

    def add_padding(self, text: bytes) -> bytes:
        padder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).padder()
        return padder.update(text) + padder.finalize()

    def encrypt_symmetric_key(self, symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        c_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None)
            )
        return c_key

    def encrypt_text(self, text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        padded_text = self.add_padding(text)
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return c_text
