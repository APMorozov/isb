from functions import read_json, read_text, write_text
from task1.vigenere import vigenere, decode_vigenere

if __name__ == "__main__":
    try:
        settings_task1 = read_json('settings.json').get('task1')
        key_task1 = read_json(settings_task1['key'])
        alphabets = read_json(settings_task1['alphabets'])
        plain_text = read_text(settings_task1["plain_text"])

        encrypted_text = vigenere(plain_text, key_task1['key'], alphabets["RU"])
        print(encrypted_text)
        decrypted_text = decode_vigenere(encrypted_text, key_task1['key'], alphabets["RU"])
        print(decrypted_text)

        write_text(settings_task1["encrypted_text"], encrypted_text)
    except Exception as exc:
        raise Exception(f"Error: {exc}")
