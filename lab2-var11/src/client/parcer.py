from LxmlSoup import LxmlSoup
import requests


def parce_random(url: str) -> str:
    """
    Parce sequence from Random.org.
    Args:
        url: url

    Returns: sequence

    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = LxmlSoup(response.text)
            link = soup.find_all('span')
            number = link[0].text()
            sequence = ''.join(number.splitlines())
            return sequence
        else:
            raise Exception("Error:", response.status_code)
    except Exception as exp:
        print(f"ERROR! {exp}")

