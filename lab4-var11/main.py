from task.CrackHash import CrackHash
from task.file_work import read_json

if __name__ == "__main__":
    settings = read_json("settings.json")
    start_const = settings["start_const"]
    card_number = "5520609999992315"

    print(f"Target hash: {start_const["hash"]}")

    result = ""

    for bin in start_const["tbank_mastercard_bins"]:
        result = CrackHash.find_collision(bin, start_const["last_four"], start_const["hash"], 14)
        if result is not None:
            print(f"Result: {result}")
            break

    check_number = CrackHash.luhn_algorithm(result)
    print(check_number)


