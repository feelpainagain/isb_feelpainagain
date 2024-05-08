import logging
import math
from work_files import*

import mpmath

logging.basicConfig(level=logging.INFO)

PI = {1: 0.2148, 2: 0.3672, 3: 0.2305, 4: 0.1875}


def bitwise_test(sequence) -> float:

    try:
        sum = 0
        for i in sequence:
            if int(i) == 1:
                sum += 1
            else:
                sum -= 1
        sum = math.fabs(sum) / math.sqrt(len(sequence))
        p_value = math.erfc(sum / math.sqrt(2))
        return p_value
    except Exception as ex:
        logging.error(f"ZeroDivisionError: {ex.message}\n{ex.args}\n")


def same_bits_test(sequence) -> float:

    try:
        counter = sequence.count("1")
        counter *= 1 / len(sequence)
        if abs(counter - 0.5) < 2 / math.sqrt(len(sequence)):
            v = 0
            for i in range(len(sequence) - 1):
                if sequence[i] != sequence[i + 1]:
                    v += 1
            num = abs(v - 2 * len(sequence) * counter * (1 - counter))
            denom = 2 * math.sqrt(2 * len(sequence)) * counter * (1 - counter)
            p_value = math.erfc(num / denom)
        else:
            p_value = 0
        return p_value
    except Exception as ex:
        logging.error(f"ZeroDivisionError: {ex.message}\n{ex.args}\n")


def split_bits(sequence) -> list:

    blocks = []
    quantity = len(sequence) - (len(sequence) % 8)
    for i in range(0, quantity, 8):
        block = sequence[i : i + 8]
        blocks.append(block)
    return blocks


def largest_number_of_units(blocks: list) -> dict:

    try:
        unit_counts = {}
        for block in blocks:
            counter = 0
            max_counter = 0
            for i in block:
                if int(i) == 1:
                    counter += 1
                    max_counter = max(max_counter, counter)
                    if max_counter > 4:
                        max_counter = 4
                else:
                    counter = 0
            if max_counter in unit_counts:
                unit_counts[max_counter] += 1
            else:
                unit_counts[max_counter] = 1
        sorted_dict = dict(sorted(unit_counts.items(), key=lambda x: x[1]))
        return sorted_dict
    except Exception as ex:
        logging.error(f"TypeError block wasn't str: {ex.message}\n{ex.args}\n")


def length_test(dictionary: dict) -> float:
 
    try:
        square_x = 0
        for i, value in dictionary.items():
            square_x += pow(value - 16 * PI[i], 2) / (16 * PI[i])
        p_value = mpmath.gammainc(3 / 2, square_x / 2)
        return p_value
    except Exception as ex:
        logging.error(
            f"Length of the dictionary is longer than number of pi-constants: {ex.message}\n{ex.args}\n"
        )


if __name__ == "__main__":

    sequence_java = read_text('sequence_java.txt')
    print(bitwise_test(sequence_java))
    print(same_bits_test(sequence_java))
    print(
        length_test(
            largest_number_of_units(split_bits(sequence_java))
        )
    )
    sequence_cpp = read_text('sequence_cpp.txt')
    print(bitwise_test(sequence_cpp))
    print(same_bits_test(sequence_cpp))
    print(
        length_test(
            largest_number_of_units(split_bits(sequence_cpp))
        )
    )
    