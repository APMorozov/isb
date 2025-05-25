import itertools
from typing import Generator
import multiprocessing as mp
import hashlib


class CrackHash:
    """
    class have method for crack hash of bank card
    """

    @staticmethod
    def generate_numbers(bin: str, last_four: str, length: int = 16) -> Generator[str, None, None]:
        """
        generate card numbers by mask bin + unknown part + last four numbers
        :param bin: bin numbers
        :param last_four: last four numbers
        :param length: len of card`s number
        :return: Generator with all generated card numbers
        """
        len_miss_part = length - len(bin) - len(last_four)
        for miss_part in itertools.product("0123456789", repeat=len_miss_part):
            yield bin + "".join(miss_part) + last_four

    @staticmethod
    def get_count_cores() -> int:
        """
        get cores count for your system
        :return: cores count
        """
        return mp.cpu_count()

    @staticmethod
    def check_number(pair: tuple[str, str]) -> str | None:
        """
        compares generated card`s number hash with target hash
        :param pair: pair string [target_hash, card`s number]
        :return: if targen hash == card hash -> card`s number, else -> None
        """
        target_hash, card_number = pair
        current_hash = hashlib.sha512(card_number.encode()).hexdigest()
        if current_hash == target_hash:
            return card_number
        return None

    @staticmethod
    def find_collision(bin: list[str], last_four: str, target_hash: str, num_process: int = 3) -> str | None:
        """
        find collision by brute force
        :param bin: bin
        :param last_four: last four
        :param target_hash: hash which will be cracked
        :param num_process: num of process
        :return: if hash cracked -> card number, else -> None
        """
        if num_process != 3:
            num_process = min(mp.cpu_count(), 3)

        with mp.Pool(processes=num_process) as pool:
            numbers = CrackHash.generate_numbers(bin, last_four)
            pairs = ((target_hash, num) for num in numbers)

            for i, result in enumerate(pool.map(CrackHash.check_number, pairs)):
                if i % 10000 == 0:
                    print(f"Checked {i} numbers")

                if result is not None:
                    pool.terminate()
                    return result
        return None

    @staticmethod
    def luhn_algorithm(card_number: str) -> bool:
        """
        Luhn`s algorithm
        :param card_number: card number
        :return:  card number is correct or not
        """
        total = 0
        for i, digit in enumerate(reversed(card_number)):
            num = int(digit)
            if i % 2 == 1:
                num *= 2
                if num > 9:
                    num = num // 10 + num % 10
            total += num
        return total % 10 == 0


