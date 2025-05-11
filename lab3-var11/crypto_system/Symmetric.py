from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as symmetric_padding
import os


class Symmetric:

    @staticmethod
    def get_iv() -> bytes:
        return os.urandom(algorithms.Camellia.block_size // 8)

    @staticmethod
    def gen_symmetric(len_key: int) -> bytes:
        """
        Generate random symmetric key
        :param len_key: len of key
        :return: key
        """
        key = os.urandom(len_key // 8)
        return key

    @staticmethod
    def add_padding(text: bytes) -> bytes:
        padder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).padder()
        return padder.update(text) + padder.finalize()

    @staticmethod
    def unpadding(text: bytes) -> bytes:
        unpadder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).unpadder()
        return unpadder.update(text) + unpadder.finalize()

    @staticmethod
    def encrypt_text(text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        padded_text = Symmetric.add_padding(text)
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return c_text

    @staticmethod
    def decript_text(text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        return Symmetric.unpadding(dc_text)

