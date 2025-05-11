from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
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
        """
        add padding to text
        :param text: text to which padding is added
        :return: text with padding
        """
        padder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).padder()
        return padder.update(text) + padder.finalize()

    @staticmethod
    def unpadding(text: bytes) -> bytes:
        """
        delete padding from text
        :param text: text to which padding is deleted
        :return: text without padding
        """
        unpadder = symmetric_padding.PKCS7(algorithms.Camellia.block_size).unpadder()
        return unpadder.update(text) + unpadder.finalize()

    @staticmethod
    def encrypt_text(text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        """
        Encrypt text by Cameliia
        :param text: plain text
        :param symmetric_key: key
        :param iv: initialization vector
        :return: encrypted_text
        """
        padded_text = Symmetric.add_padding(text)
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        return c_text

    @staticmethod
    def decrypt_text(text: bytes, symmetric_key: bytes, iv: bytes) -> bytes:
        """
        Decrypt encrypted text by Cameliia
        :param text: encrypted text
        :param symmetric_key: key
        :param iv: initialization vector
        :return: decrypted text
        """
        cipher = Cipher(algorithms.Camellia(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        return Symmetric.unpadding(dc_text)

