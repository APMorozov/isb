from func import get_response, read_json, write_json
from parcer import parce_random
from tests import bit_frequency_test, consecutive_bits_test, longest_sequence_block


class App:
    def __init__(self):
        self._is_work = True
        self._settings = read_json("settings.json")
        self._p_value_threshold = self._settings["p_value_threshold"]
        self._urls = read_json(self._settings["urls"])
        self._pi_i = self._settings["pi_i"]

    def _print_old_sequences(self) -> None:
        """
        print sequences from the file specified by the path from the settings
        Returns: None

        """
        try:
            sequences = read_json(self._settings["sequences"])
            print(f"C++ sequence {sequences["c++_sequence"]}")
            print(f"Java sequence {sequences["java_sequence"]}")
            print(f"Random.org sequence {sequences["random.org_sequence"]}")
        except Exception as exc:
            print("Error!Can not print sequences. ", exc)

    def _start_print(self) -> None:
        """
        print options of action
        Returns: None

        """
        print("Request action:")
        print("1)Get sequences(c++, java, random.org)")
        print("2)Use sequences(file: sequences.json)")
        print("3)Print sequences")
        print("4)Exit")

    def _check_sequence(self, sequence_name: str) -> bool:
        """
        checks sequences according to NIST tests
        Args:
            sequence_name: name of key in json file

        Returns: random or not

        """
        sequences = read_json(self._settings["sequences"])
        sequence = sequences[sequence_name]

        tests = [
            ("Bit Frequency Test", bit_frequency_test(sequence)),
            ("Consecutive Bits Test", consecutive_bits_test(sequence)),
            ("Longest Sequence Block", longest_sequence_block(sequence,self._pi_i))
        ]

        flag = True
        for test_name, result in tests:
            print(f"{test_name}: {result}")
            if result < self._p_value_threshold:
                flag = False

        return flag

    def _take_new_sequences(self) -> None:
        """
        take new sequences by urls and write data in sequences.json
        Returns: None

        """
        try:
            json_data1 = get_response(self._urls["c++_server_url"])

            json_data2 = get_response(self._urls["java_server_url"])

            sequence = parce_random((self._urls["random.org_url"]))
            sequences = ({"c++_sequence": json_data1["sequence"], "java_sequence": json_data2["sequence"],
                          "random.org_sequence": sequence})
            write_json(self._settings["sequences"], sequences)
        except Exception as exc:
            print("Error!Can not take sequences. ", exc)

    def _check_c_plus_plus_seq(self) -> bool:
        """
        Check C++ sequence
        Returns: random or not

        """
        return self._check_sequence("c++_sequence")

    def _check_java_seq(self) -> bool:
        """
        Check Java sequence
        Returns: random or not

        """
        return self._check_sequence("java_sequence")

    def _check_random_seq(self) -> bool:
        """
        Check Random.org sequence
        Returns: random or not

        """
        return self._check_sequence("random.org_sequence")

    def _check_sequences(self) -> None:
        """
        Check 3 sequences in 1 func
        Returns: None

        """
        try:
            if self._check_c_plus_plus_seq():
                print("C++ sequence is random\n")
            if self._check_java_seq():
                print("Java sequence is random\n")
            if self._check_random_seq():
                print("Random.org sequence is random\n")

        except Exception as exc:
            print("Error!Can not check sequences. ", exc)

    def _space(self) -> None:
        """
        get space in terminal
        Returns: None

        """
        print("\n" * 3)

    def start(self) -> None:
        """
        This method includes all the others. It launches the console application
        Returns: None

        """
        while self._is_work:
            self._start_print()
            action = input("Input number 1-4: ")
            self._space()
            match action:
                case '1':
                    self._take_new_sequences()
                    print("sequences taken")
                case '2':
                    self._check_sequences()
                case '3':
                    self._print_old_sequences()
                case '4':
                    self._is_work = False
                case _:
                    print("Input number 1-4!!!")
