import json


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


def read_txt(path: str) -> bytes:
    try:
        with open(path, "rb") as file:
            return file.read()
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")
