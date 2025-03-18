from functions import read_json, read_text, write_text, sort_json
from task1.vigenere import vigenere, decode_vigenere
from task2.freq_decod import get_freq, decode

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

        settings_task2 = read_json('settings.json').get('task2')
        encrypted_text_t2 = read_text(settings_task2['plain_text'])
        get_freq(encrypted_text_t2, settings_task2['frequenceFile'])
        sort_json(settings_task2['frequenceFile'])
        decode(encrypted_text_t2, settings_task2['decrypted_text'], settings_task2["mappingFileToRu"])
    except Exception as exc:
        raise Exception(f"Error: {exc}")
