import json


def read_json(path: str) -> tuple[str, str]:
    """
    Read json file
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
    write data to json file
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


def sort_json(path: str) -> None:
    """
    sort json file and rewrite them
    :param path: path to json file
    :return: None
    """
    data = read_json(path)
    data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    write_json(path, data)


def read_text(path: str) -> str:
    """
    read text file
    :param path: path to txt file
    :return: str with data
    """
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File wasn`t found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")


def write_text(path: str, data: str) -> None:
    """
    write data to txt file
    :param path: path to file
    :param data: data which will be written in file
    :return: None
    """
    try:
        with open(path, mode="w", encoding="utf-8") as file:
            file.write(data)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File wasn`t found: {not_found}")
    except Exception as exc:
        raise Exception(f"An error occurred when opening the file {exc}")
