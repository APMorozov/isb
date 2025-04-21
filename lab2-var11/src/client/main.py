from App import App
from func import read_json
from tests import bit_frequency_test, consecutive_bits_test

def main() -> int:
    settings = read_json("settings.json")
    sequences = read_json(settings["sequences"])
    bit_frequency_test(sequences["c++_sequence"])
    bit_frequency_test(sequences["java_sequence"])
    bit_frequency_test(sequences["random.org_sequence"])
    consecutive_bits_test(sequences["c++_sequence"])
    consecutive_bits_test(sequences["java_sequence"])
    consecutive_bits_test(sequences["random.org_sequence"])
    #myapp = App()
    #myapp.start()
    return 0


if __name__ == '__main__':
        main()