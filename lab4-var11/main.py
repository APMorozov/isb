from task.CrackHash import CrackHash
from task.file_work import read_json, write_json
from task.time_meter import time_meter
from task.visualization import plot

if __name__ == "__main__":
    settings = read_json("settings.json")
    start_const = settings["start_const"]
    card_number = "5520609999992315"

    print(f"Target hash: {start_const["hash"]}")

    time_result = time_meter(start_const["tbank_mastercard_bins"], start_const["last_four"], start_const["hash"])
    print(f"Time result: {time_result}")
    write_json(time_result, "task/time_results.json")

    plot(time_result)