from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


class Asymmetric:
    def gen_asymmetric(self) -> tuple:
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = keys.public_key()
        return public_key, keys
    def decrypt_symmetric_key(self, decrypted_symmetric_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        dc_text = private_key.decrypt(decrypted_symmetric_key,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                    algorithm=hashes.SHA256(), label=None))
        return dc_text

    def encrypt_symmetric_key(self, symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        c_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None)
        )
        return c_key
