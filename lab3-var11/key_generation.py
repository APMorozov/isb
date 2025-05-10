import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def gen_symmetric(len_key: int) -> bytes:
    """
    Generate random symmetric key
    :param len_key: len of key
    :return: key
    """
    key = os.urandom(len_key // 8)
    return key


def serialize_symmetric(path: str, symmetric_key: bytes) -> None:
    try:
        with open(path, "wb") as file:
            file.write(symmetric_key)
    except Exception as exc:
        raise Exception(f"Error!!!Serialize symmetric key: {exc}")


def deserialize_symmetric(path: str) -> bytes:
    try:
        with open(path, "rb") as file:
            return file.read()
    except Exception as exc:
        raise Exception(f"Error!!!Serialize symmetric key: {exc}")


class Asymmetric:
    def gen_asymmetric(self) -> tuple:
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = keys.public_key()
        return public_key, keys

    def serialize_public(self, file_path: str, public_key: rsa.RSAPublicKey) -> None:
        """
        Serialize private key and write it in file
        :param file_path: path to file where was written key
        :param public_key: public RSA key
        :return: None
        """
        try:
            with open(file_path, 'wb') as file:
                file.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo
                    )
                )
        except Exception as exc:
            raise Exception(f"Error!!!Serialize public key: {exc}")

    def serialize_private(self, file_path: str, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serialize private key and write it in file
        :param file_path: path to file where was written key
        :param private_key: private RSA key
        :return: None
        """
        try:
            with open(file_path, 'wb') as file:
                file.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption()
                    )
                )
        except Exception as exc:
            raise Exception(f"Error!!!Serialize private key: {exc}")

    def deserialize_public(self, file_path: str) -> rsa.RSAPublicKey:
        try:
            with open(file_path, 'rb') as file:
                public_bytes = file.read()
                d_public_key = load_pem_public_key(public_bytes)
                return d_public_key
        except Exception as exc:
            raise Exception(f"Error!!!Deserialize public key: {exc}")

    def deserialize_private(self, file_path: str) -> rsa.RSAPrivateKey:
        try:
            with open(file_path, 'rb') as file:
                public_bytes = file.read()
                d_public_key = load_pem_private_key(public_bytes, password=None)
                return d_public_key
        except Exception as exc:
            raise Exception(f"Error!!!Deserialize public key: {exc}")
