from crypto_system.file_work import (read_json, read_txt, write_bytes_txt, write_text_txt, serialize_public, serialize_private, serialize_symmetric,
                                     deserialize_public, deserialize_private, deserialize_symmetric)
from crypto_system.Asymmetric import Asymmetric
from crypto_system.Symmetric import Symmetric
import os


class App:

    def __init__(self):
        try:
            self._settings = read_json("settings/settings.json")
            self._is_work = True
            self._iv = Symmetric.get_iv()
        except Exception as exp:
            print("Can not find setting file in default path!!!You can input new path.")

    def start_message(self):
        print("Request action:")
        print("1)Get path to settings.json file")
        print("2)Generate keys")
        print("3)Encrypt text by symmetric key")
        print("4)Decrypt ciphered text")
        print("5)Exit")
        print("Input number 1-5:")

    def space(self) -> None:
        print('\n' * 3)

    def app(self):
        while self._is_work:
            self.start_message()
            action = input()
            self.space()
            match action:
                case "1":
                    try:
                        print("Input path to settings.json file:")
                        path = input()
                        self._settings = read_json(path)
                    except Exception as exc:
                        print(f"Error!Can not read settings file: {exc}")
                case "2":
                    try:
                        asym_keys = Asymmetric.gen_asymmetric()
                        sym_key = Symmetric.gen_symmetric(self._settings["len_of_key"])
                        serialize_public(self._settings["keys"]["public_key"], asym_keys[0])
                        serialize_private(self._settings["keys"]["private_key"], asym_keys[1])
                        d_sym_key = Asymmetric.encrypt_symmetric_key(sym_key, asym_keys[0])
                        serialize_symmetric(self._settings["keys"]["encrypt_symmetric_key"], d_sym_key)
                        print("Keys generated!")
                    except Exception as exc:
                        print(f"Error!!!Keys was not generated: {exc}")
                case "3":
                    try:
                        text = read_txt(self._settings["texts"]["plain_text"])
                        enc_sym_key = deserialize_symmetric(self._settings["keys"]["encrypt_symmetric_key"])
                        dec_sym_key = Asymmetric.decrypt_symmetric_key(enc_sym_key, deserialize_private(self._settings["keys"]["private_key"]))
                        c_text = Symmetric.encrypt_text(text, dec_sym_key, self._iv)
                        write_bytes_txt(self._settings["texts"]["encrypted_text"], c_text)
                        print("Text encrypted")
                    except Exception as exc:
                        print(f"Error!!!Text was not encrypt: {exc}")
                case "4":
                    try:
                        enc_text = read_txt(self._settings["texts"]["encrypted_text"])
                        enc_sym_key = deserialize_symmetric(self._settings["keys"]["encrypt_symmetric_key"])
                        dec_sym_key = Asymmetric.decrypt_symmetric_key(enc_sym_key, deserialize_private(self._settings["keys"]["private_key"]))
                        dec_text = Symmetric.decript_text(enc_text, dec_sym_key, self._iv)
                        write_text_txt(self._settings["texts"]["decrypted_text"], dec_text.decode("UTF-8"))
                        print("Text decrypted")
                    except Exception as exc:
                        print(f"Error!!!Text was not decrypt: {exc}")
                case "5":
                    self._is_work = False
                case _:
                    print("Error!Input number in range 1-5")