import os

from crypto_system.file_work import (read_json, read_txt, serialize_public, serialize_private, serialize_symmetric,
                                     deserialize_public, deserialize_private, deserialize_symmetric)
from crypto_system.Symmetric import Symmetric
from crypto_system.Asymmetric import Asymmetric


if __name__ == "__main__":
    asym = Asymmetric()
    sym = Symmetric()
    symmetric_key = sym.gen_symmetric(128)
    keys = asym.gen_asymmetric()
    iv = os.urandom(16)

    settings = read_json("settings//settings.json")
    path_file_keys = settings["keys"]
    path_file_txt = settings["texts"]
    text = read_txt(path_file_txt["plain_text"])

    serialize_public(path_file_keys["public_key"], keys[0])
    serialize_private(path_file_keys["private_key"], keys[1])

    c_text = sym.encrypt_text(text, symmetric_key, iv)
    enc_sym_key = asym.encrypt_symmetric_key(symmetric_key, deserialize_public(path_file_keys["public_key"]))
    serialize_symmetric(path_file_keys["encrypt_symmetric_key"], enc_sym_key)
    new_enc_sym_key = deserialize_symmetric(path_file_keys["encrypt_symmetric_key"])
    new_sym_key = asym.decrypt_symmetric_key(new_enc_sym_key, deserialize_private(path_file_keys["private_key"]))
    dc_text = sym.decript_text(c_text, new_sym_key, iv)
    print(dc_text.decode("UTF-8"))
