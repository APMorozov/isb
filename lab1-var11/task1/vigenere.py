def vigenere(plain_text: str, key: str, alphabet: str) -> str:
    """
    This func encrypt plain_text by vigenere cipher with key and alphabet
    :param plain_text: start text
    :param key: key for encrypt
    :param alphabet: open alphabet
    :return: encrypted text
    """
    match plain_text, key, alphabet:
        case '', key, alphabet:
            return plain_text
        case plain_text, '' | '':
            print('ERROR!Key or alphabet can`t be empty')
        case _:
            plain_text_tolower = plain_text.lower()
            key_tolower = key.lower()
            alphabet_dict = {symbol: index for index, symbol in enumerate(alphabet)}
            print(alphabet_dict)
            encrypted_answer = ''

            for i in range(len(plain_text_tolower)):
                current_key = i % len(key_tolower)
                sum_of_idx = alphabet_dict.get(plain_text_tolower[i]) + alphabet_dict.get(key_tolower[current_key])
                match sum_of_idx:
                    case sum_of_idx if sum_of_idx >= len(alphabet):
                        decode_symbol = sum_of_idx - len(alphabet)
                        encrypted_answer += alphabet[decode_symbol]
                    case sum_of_idx:
                        encrypted_answer += alphabet[sum_of_idx]
            return encrypted_answer


def decode_vigenere(encrypted_text: str, key: str, alphabet: str) -> str:
    """
        This func decode encrypted_text by vigenere cipher with key and alphabet
        :param encrypted_text: start text
        :param key: key for encrypt
        :param alphabet: open alphabet
        :return: decoded text
        """
    match encrypted_text, key, alphabet:
        case '', key, alphabet:
            return encrypted_text
        case encrypted_text, '' | '':
            print('ERROR!Key or alphabet can`t be empty')
        case _:
            alphabet_dict = {symbol: index for index, symbol in enumerate(alphabet)}
            decoded_answer = ''
            encrypted_text_tolower = encrypted_text.lower()
            key_tolower = key.lower()
            for i in range(len(encrypted_text)):
                current_key = i % len(key)
                diff_of_idx = alphabet_dict.get(encrypted_text_tolower[i]) - alphabet_dict.get(key_tolower[current_key])
                match diff_of_idx:
                    case diff_of_idx if diff_of_idx < 0:
                        decode_symbol = diff_of_idx + len(alphabet)
                        decoded_answer += alphabet[decode_symbol]
                    case diff_of_idx:
                        decoded_answer += alphabet[diff_of_idx]
            return decoded_answer
