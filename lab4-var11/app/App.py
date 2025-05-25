from task.CrackHash import CrackHash
from task.file_work import read_json, write_json, write_txt
from task.time_meter import time_meter
from task.visualization import plot

from tqdm import tqdm


class App:

    def __init__(self, path_to_settings: str) -> None:
        """
        CTOR
        :param path_to_settings: path to file json
        """
        self._is_work = True
        self._settings = read_json(path_to_settings)
        self._path_time_result = "task/time_results.json"
        self._cores_count = 5
        self._time_result = None
        self._crack_result = None

    @staticmethod
    def start_message() -> None:
        """
        start message
        :return: None
        """
        print("Select action:")
        print("1)Input path to settings(json file)")
        print("2)Input path to file with time test result")
        print("3)Crack hash")
        print("4)Start time test")
        print("5)Input count cores for crack hash")
        print("6)Show plot")
        print("7)Check card number by Luhn algorithm")
        print("8)Exit")
        print("Input number in range [1;8]: ")

    def crack_hash(self) -> None:
        """
        Crack hash
        :return: None
        """
        for bin in tqdm(self._settings["start_const"]["tbank_mastercard_bins"]):
            self._crack_result = CrackHash.find_collision(
                bin,
                self._settings["start_const"]["last_four"],
                self._settings["start_const"]["hash"]
            )
            if self._crack_result is not None:
                print(f"Hash cracked card, number is: {self._crack_result}")
                write_txt(self._crack_result, self._settings["start_const"]["path_to_result"])
                break

    def run(self) -> None:
        """
        start app
        :return: None
        """
        while self._is_work:
            self.start_message()
            action = input()
            match action:
                case "1":
                    try:
                        path_to_settings = input("Input path: ")
                        self._settings = read_json(path_to_settings)
                    except Exception as exc:
                        print(f"ERROR!!!Read settings json file: {exc}")
                case "2":
                    try:
                        self._path_time_result = input("Input path: ")
                        self._time_result = read_json(self._path_time_result)
                    except Exception as exc:
                        print(f"ERROR!!!Read time result json file: {exc}")
                case "3":
                    try:
                        self.crack_hash()
                    except Exception as exc:
                        print(f"ERROR!!!Can not crack hash: {exc}")
                case "4":
                    try:
                        self._time_result = time_meter(
                            self._settings["start_const"]["tbank_mastercard_bins"],
                            self._settings["start_const"]["last_four"],
                            self._settings["start_const"]["hash"]
                        )
                        write_json(self._time_result, self._path_time_result)
                    except Exception as exc:
                        print(f"ERROR!!!In time test: {exc}")

                case "5":
                    cores_count = input("Input cores count: ")
                    if int(cores_count) in range(1, 150):
                        self._cores_count = cores_count
                    else:
                        print("Count of cores must be in range [1,149]")
                case "6":
                    try:
                        if self._time_result is not None:
                            plot(self._time_result)
                        else:
                            self._time_result = read_json(self._path_time_result)
                            plot(self._time_result)
                    except Exception as exc:
                        print(f"ERROR!!!In plot: {exc}")
                case "7":
                    try:
                        if self._crack_result is not None:
                            luhn_result = CrackHash.luhn_algorithm(self._crack_result)
                            print(f"Card number correct: {luhn_result}")
                        else:
                            print("Can not find card number")
                    except Exception as exc:
                        print(f"ERROR!!!In Luhn algorithm {exc}")
                case "8":
                    print("Exit")
                    self._is_work = False
                case _:
                    print("ERROR!!!Input number in range [1;8]")



