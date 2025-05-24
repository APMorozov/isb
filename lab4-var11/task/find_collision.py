import itertools
from typing import Generator
import multiprocessing as mp
import hashlib


class FindCollision:

    @staticmethod
    def generate_number(bin: str, last_four: str) -> Generator[str, None, None]:
        generated_len = 16 - len(bin) - len(last_four)
        for generated in itertools.product("0123456789", repeat=generated_len):
            yield bin + "".join(generated) + last_four

    @staticmethod
    def get_count_cores():
        return mp.cpu_count()

    @staticmethod
    def check_number(hash: str, card_number: str):
        new_hash = hashlib.sha512(card_number.encode()).hexdigest()
        print(new_hash)
        return new_hash == hash

    @staticmethod
    def find_collision(bins: list[str], last_four: str, hash: str) -> str:
        with mp.Pool(processes=FindCollision.get_count_cores()) as p:
            for bin in bins:
                for generated_numbers in p.map(FindCollision.generate_number(bin,last_four)):
                    print("231")
