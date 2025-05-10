import os

from key_generation import gen_symmetric, Asymmetric, serialize_symmetric, deserialize_symmetric
from file_work import read_json, read_txt
from encryption import Encryption
from decription import Decription


if __name__ == "__main__":
    symmetric_key = gen_symmetric(128)
    asym = Asymmetric()
    enc = Encryption()
    dec = Decription()
    keys = asym.gen_asymmetric()
    iv = os.urandom(16)

    settings = read_json("settings//settings.json")
    path_file_keys = settings["keys"]
    path_file_txt = settings["texts"]
    text = read_txt(path_file_txt["plain_text"])

    asym.serialize_public(path_file_keys["public_key"], keys[0])
    asym.serialize_private(path_file_keys["private_key"], keys[1])

    c_text = enc.encrypt_text(text, symmetric_key, iv)
    enc_sym_key = enc.encrypt_symmetric_key(symmetric_key, asym.deserialize_public(path_file_keys["public_key"]))
    serialize_symmetric(path_file_keys["encrypt_symmetric_key"], enc_sym_key)
    new_enc_sym_key = deserialize_symmetric(path_file_keys["encrypt_symmetric_key"])
    new_sym_key = dec.decrypt_symmetric_key(new_enc_sym_key, asym.deserialize_private(path_file_keys["private_key"]))
    dc_text = dec.decription(c_text, new_sym_key, iv)
    print(dc_text.decode("UTF-8"))
