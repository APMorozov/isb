from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as symmetric_padding
import os


class Symmetric:

    def gen_symmetric(self, len_key: int) -> bytes:
        """
        Generate random symmetric key
        :param len_key: len of key
        :return: key
        """
        key = os.urandom(len_key // 8)
        return key

    def add_padding(self, text: bytes) -> bytes:
        padder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).padder()
        return padder.update(text) + padder.finalize()

    def unpadding(self, text: bytes) -> bytes:
        unpadder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).unpadder()
        return unpadder.update(text) + unpadder.finalize()

    def encrypt_text(self, text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        padded_text = self.add_padding(text)
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return c_text

    def decript_text(self, text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        return self.unpadding(dc_text)

