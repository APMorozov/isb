import json


def write_json(results: list[list[int | float]], filename: str) -> None:
    """
    write info to json file
    :param results: data
    :param filename: path to file
    :return: None
    """
    try:
        with open(filename, 'w') as f:
            json.dump(results, f)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")


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


def write_txt(text: str, filename: str) -> None:
    """
    write data to txt file
    :param text: data
    :param filename: path to file
    :return: None
    """
    try:
        with open(filename, 'w') as f:
            f.write(text)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File was not found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")