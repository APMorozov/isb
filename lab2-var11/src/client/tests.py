import math

import scipy.special


def bit_frequency_test(sequence: str):
    """
    NIST test.Performs bit frequency analysis in a binary sequence.
    Args:
        sequence: random binary sequence

    Returns: the probability that the sequence is random

    """

    x_i = 0
    for ch in sequence:
        match ch:
            case '0':
                x_i += -1
            case '1':
                x_i += 1
    s_n = abs(x_i) / math.sqrt(len(sequence))
    return math.erfc(s_n / math.sqrt(2))


def consecutive_bits_test(sequence: str) -> float:
    """
    Checks a sequence for identical consecutive bits.
    Args:
        sequence: random binary sequence

    Returns: the probability that the sequence is random

    """
    n = len(sequence)
    p = sequence.count('1') / n
    if abs(p - 0.5) < (2 / math.sqrt(n)):
        v = 0
        for i in range(n-1):
            if sequence[i] != sequence[i+1]:
                v += 1
        pvalue = math.erfc(abs(v - 2 * n * p * (1 - p)) / (2 * math.sqrt(2 * n) * p * (1 - p)))
        return pvalue


def longest_sequence_block(sequence: str) -> float:
    """
    Splits the sequence into 8-bit blocks.Distributes blocks into groups based on the maximum length '1'.
    Compute probability.
    Args:
        sequence: random binary sequence

    Returns: the probability that the sequence is random

    """
    v_i = [0, 0, 0, 0]
    pi_i = [0.2148, 0.3672, 0.2305, 0.1875]
    start = 0
    while start != len(sequence):
        max_count = 0
        current_count = 0
        sub_seq = sequence[start:start + 8]
        for i in range(8):
            if sub_seq[i] == '1':
                current_count += 1
                max_count = max(current_count, max_count)
            else:
                current_count = 0
        match max_count:
            case 0 | 1:
                v_i[0] += 1
            case 2 | 3:
                v_i[max_count-1] += 1
            case _:
                v_i[3] += 1
        start += 8
    hi_2 = 0.0
    for i in range(4):
        hi_2 += pow(v_i[i] - 16 * pi_i[i], 2) / (16 * pi_i[i])
    pvalue = scipy.special.gammainc(3/2, (hi_2/2))
    return pvalue

