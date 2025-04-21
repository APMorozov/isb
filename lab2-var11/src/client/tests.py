import math
from math import erfc, sqrt



def bit_frequency_test(sequence: str):
    x_i = 0
    for ch in sequence:
        match ch:
            case '0':
                x_i += -1
            case '1':
                x_i += 1
    s_n = 0.0
    s_n = abs(x_i) / math.sqrt(len(sequence))
    return math.erfc(s_n / math.sqrt(2))


def consecutive_bits_test(sequence: str):
    n = len(sequence)
    p = sequence.count('1') / n
    if abs(p - 0.5) < (2 / math.sqrt(n)):
        v = 0
        for i in range(n-1):
            if sequence[i] != sequence[i+1]:
                v += 1
        pvalue = math.erfc(abs(v - 2 * n * p * (1 - p)) / (2 * math.sqrt(2 * n) * p * (1 - p)))
        print(pvalue)
