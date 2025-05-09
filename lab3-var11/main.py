import os

from key_generation import gen_symmetric, Asymmetric
from file_work import read_json, read_txt
from encryption import Encryption
from decription import Decription


if __name__ == "__main__":
    symmetric_key = gen_symmetric(128)
    asym = Asymmetric()
    keys = asym.gen_asymmetric()

    settings = read_json("settings//settings.json")
    path_file_keys = settings["keys"]
    path_file_txt = settings["texts"]

    asym.serialize_public(path_file_keys["public_key"], keys[0])
    asym.serialize_private(path_file_keys["private_key"], keys[1])

    text = read_txt(path_file_txt["plain_text"])
    #text2 = bytes(text, "UTF-8")
    enc = Encryption()
    dec = Decription()
    iv = os.urandom(16)
    c_text = enc.encrypt_text(text, symmetric_key, iv)
    print(c_text)
    dc_text = dec.decription(c_text, symmetric_key, iv)
    print(dc_text.decode("UTF-8"))
    print("Symmetric key: ", symmetric_key)
    decrypted_symmetric_key = enc.encrypt_symmetric_key(symmetric_key, keys[0])
    encrypted_symmetric_key = dec.decrypt_symmetric_key(decrypted_symmetric_key, keys[1])
    print("Decrypted symmetric key: ", encrypted_symmetric_key)
