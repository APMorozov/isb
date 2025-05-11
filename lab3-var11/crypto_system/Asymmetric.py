from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


class Asymmetric:

    @staticmethod
    def gen_asymmetric() -> tuple:
        """
        Generate asymmetric keys
        :return: tuple[public_key, private_key]
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = keys.public_key()
        return public_key, keys

    @staticmethod
    def decrypt_symmetric_key(encrypted_symmetric_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
        Decrypt symmetric key
        :param encrypted_symmetric_key: symmetric key
        :param private_key: private key
        :return: decrypted symmetric key
        """
        dc_text = private_key.decrypt(encrypted_symmetric_key,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(), label=None))
        return dc_text

    @staticmethod
    def encrypt_symmetric_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
        Encrypt symmetric key
        :param symmetric_key: symmetric key
        :param public_key: public key
        :return: encrypted symmetric key
        """
        c_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None)
        )
        return c_key
