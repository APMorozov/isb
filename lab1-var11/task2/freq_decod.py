from functions import write_json, read_json,write_text


def get_freq(encrypted_text: str, path_to_json):
    freq = {}
    for elm in encrypted_text:
        freq[elm] = 0
        for i in encrypted_text:
            if i == elm:
                freq[elm] += 1
        freq[elm] = freq[elm] / len(encrypted_text)
    write_json(path_to_json, freq)


def decode(encrypted_text: str, path_to_file: str, path_to_map_json) -> None:
    mapping = read_json(path_to_map_json)
    data = encrypted_text
    for elm in mapping:
        print(elm)
        data = data.replace(elm, mapping.get(elm))
    write_text(path_to_file, data)
