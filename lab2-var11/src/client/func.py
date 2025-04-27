import requests
import json


def get_response(url: str) -> json:
    """
    get sequences from url.
    Args:
        url: url where server hosted

    Returns: json{"sequence": value }

    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            raise Exception("Error:", response.status_code)
    except Exception as exc:
        print(f"ERROR! {exc}")


def read_json(path: str) -> tuple[str, str]:
    """
    Read json file.
    :param path: path to json file
    :return: tuple of data
    """
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except json.JSONDecodeError as decode_error:
        raise ValueError(f"Error decoded the json file: {decode_error}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")


def write_json(path: str, data: dict[str, int]) -> None:
    """
    write data to json file.
    :param path: path to json file
    :param data: data to file
    :return: None
    """
    try:
        with open(path, mode="w", encoding="utf-8") as file:
            return json.dump(data, file)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")
