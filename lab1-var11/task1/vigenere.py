def vigenere(plain_text: str, key: str, alphabet: str) -> str:
    """
    This func encrypt plain_text by vigenere cipher with key and alphabet
    :param plain_text: start text
    :param key: key for encrypt
    :param alphabet: open alphabet
    :return: encrypted text
    """
    if plain_text == "":
        return plain_text
    if alphabet == "":
        raise Exception("ERROR!Alphabet can`t be empty")
    if key == "":
        raise Exception("ERROR!Key can`t be empty")

    plain_text_tolower = plain_text.lower()
    key_tolower = key.lower()
    print(plain_text_tolower)
    alphabet_dict = {symbol: index for index, symbol in enumerate(alphabet)}
    print(alphabet_dict)
    encrypted_answer = ''

    for i in range(len(plain_text_tolower)):
        current_key = i % len(key_tolower)
        if abs(alphabet_dict.get(plain_text_tolower[i]) + alphabet_dict.get(key_tolower[current_key])) >= len(alphabet):
            decode_symbol = alphabet_dict.get(plain_text_tolower[i]) + alphabet_dict.get(key_tolower[current_key]) - len(alphabet)
            encrypted_answer += alphabet[decode_symbol]
        else:
            encrypted_answer += alphabet[alphabet_dict.get(plain_text_tolower[i]) + alphabet_dict.get(key_tolower[current_key])]
    return encrypted_answer


def decode_vigenere(encrypted_text: str, key: str, alphabet: str) -> str:
    """
        This func decode encrypted_text by vigenere cipher with key and alphabet
        :param encrypted_text: start text
        :param key: key for encrypt
        :param alphabet: open alphabet
        :return: decoded text
        """
    if encrypted_text == "":
        return encrypted_text
    if alphabet == "":
        raise Exception("ERROR!Alphabet can`t be empty")
    if key == "":
        raise Exception("ERROR!Key can`t be empty")

    alphabet_dict = {symbol: index for index, symbol in enumerate(alphabet)}
    decoded_answer = ''
    for i in range(len(encrypted_text)):
        current_key = i % len(key)
        if (alphabet_dict.get(encrypted_text[i]) - alphabet_dict.get(key[current_key])) < 0:
            decode_symbol = alphabet_dict.get(encrypted_text[i]) - alphabet_dict.get(key[current_key]) + len(alphabet)
            decoded_answer += alphabet[decode_symbol]
        else:
            decoded_answer += alphabet[alphabet_dict.get(encrypted_text[i]) - alphabet_dict.get(key[current_key])]
    return decoded_answer
