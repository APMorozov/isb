from func import get_response, read_json, write_json
from parcer import parce_random


class App:
    is_work = True
    settings = read_json("settings.json")
    urls = read_json(settings["urls"])

    def print_old_sequences(self):
        sequences = read_json(self.settings["sequences"])
        print(f"C++ sequence {sequences["c++_sequence"]}")
        print(f"Java sequence {sequences["java_sequence"]}")
        print(f"Random.org sequence {sequences["random.org_sequence"]}")

    def start_print(self):
        print("Request action:")
        print("1)Get sequences(c++, java, random.org)")
        print("2)Use sequences(file: sequences.json)")
        print("3)Print sequences")
        print("4)Exit")

    def take_new_sequences(self):
        json_data1 = get_response(self.urls["c++_server_url"])

        json_data2 = get_response(self.urls["java_server_url"])

        sequence = parce_random((self.urls["random.org_url"]))
        sequences = ({"c++_sequence": json_data1["sequence"], "java_sequence": json_data2["sequence"],
                      "random.org_sequence": sequence})
        write_json("sequences.json", sequences)

    def cls(self):
        print("\n" * 100)

    def start(self):
        while self.is_work:
            self.start_print()
            action = input("Input number 1-4 ")
            self.cls()
            match action:
                case '1':
                    self.take_new_sequences()
                    print("sequences taken")
                case '2':
                    print("Case 2")
                case '3':
                    self.print_old_sequences()
                case '4':
                    self.is_work = False
                case _:
                    print("Input number 1-4 ")
