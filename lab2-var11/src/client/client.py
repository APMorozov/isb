from func import get_response, read_json
from parcer import parce_random

import requests


def main():
    urls = read_json("urls.json")
    json_data1 = get_response(urls["c++_server_url"])

    json_data2 = get_response(urls["java_server_url"])

    sequence = parce_random((urls["random.org_url"]))
    print(sequence)
    print(json_data1)
    print(json_data2)


if __name__ == '__main__':
        main()
