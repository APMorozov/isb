import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def read_json(path: str) -> tuple[str, str]:
    """
    Read json file.
    :param path: path to json file
    :return: tuple of data
    """
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except json.JSONDecodeError as decode_error:
        raise ValueError(f"Error decoded the json file: {decode_error}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")


def read_txt(path: str) -> bytes:
    try:
        with open(path, "rb") as file:
            return file.read()
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the txt file {exc}")


def write_bytes_txt(path: str, text: bytes) -> None:
    try:
        with open(path, "wb") as file:
            file.write(text)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when write the txt file {exc}")


def write_text_txt(path: str, text: str) -> None:
    try:
        with open(path, "w") as file:
            file.write(text)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when write the txt file {exc}")


def serialize_public(file_path: str, public_key: rsa.RSAPublicKey) -> None:
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


def serialize_private(file_path: str, private_key: rsa.RSAPrivateKey) -> None:
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


def deserialize_public(file_path: str) -> rsa.RSAPublicKey:
    try:
        with open(file_path, 'rb') as file:
            public_bytes = file.read()
            d_public_key = load_pem_public_key(public_bytes)
            return d_public_key
    except Exception as exc:
        raise Exception(f"Error!!!Deserialize public key: {exc}")


def deserialize_private(file_path: str) -> rsa.RSAPrivateKey:
    try:
        with open(file_path, 'rb') as file:
            public_bytes = file.read()
            d_public_key = load_pem_private_key(public_bytes, password=None)
            return d_public_key
    except Exception as exc:
        raise Exception(f"Error!!!Deserialize public key: {exc}")


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
