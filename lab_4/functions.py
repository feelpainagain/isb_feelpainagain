import json
import logging
import hashlib
import multiprocessing as mp
import time

from tqdm import tqdm
from matplotlib import pyplot as plt


logging.basicConfig(level=logging.INFO)


def luna_algorithm(card_number: str) -> bool:
    """
    checks card number with luna algorithm
    args:
        card_number: number of card
    return:
        check result
    """
    try:
        card_number_list = [int(char) for char in card_number]
        for i in range(len(card_number_list) - 2, -1, -2):
            card_number_list[i] *= 2
            if card_number_list[i] > 9:
                card_number_list[i] -= 9
        return sum(card_number_list) % 10 == 0
    except Exception as ex:
        logging.error(ex)
        return False


def check_number_card(tested_part: int, hash: str, last_digits: str, bins: list) -> str | None:
    """
    func that checks if a card number is comparable to hash
    args:
        tested_part: part for tests
        hash: input hash
        last_digits: card last digits
        bins: bins
    return:
        number of card or none
    """
    for bin in bins:
        card_number = f'{bin}{tested_part:06d}{last_digits}'
        if hashlib.sha384(card_number.encode()).hexdigest() == hash:
            logging.info(f"Match found: {card_number}")
            return card_number
    return None


def number_search(save_path: str, hash: str, last_digits: str, bins: list) -> str:
    """
    func that find numbers with hash and saves it in file
    args:
        save_path: save path
        hash: input hash
        last_digits: card last 4 digits
        bins: bins
    return:
        number of card if it matches with hash
    """
    card_numbers = None
    with mp.Pool(mp.cpu_count()) as p:
        for result in p.starmap(check_number_card, [(i, hash, last_digits, bins) for i in range(0, 1000000)]):
            if result is not None:
                card_numbers = result
                break
    try:
        with open(save_path, mode='w', encoding="utf-8") as file:
            json.dump({"card_number": card_numbers}, file)
    except Exception as ex:
        logging.error(ex)
    return card_numbers


def collision_dependence(hash: str, last_digits: str, bins: list) -> None:
    """
    func that measures time for collisions and makes time dependence
    args:
        hash: input hash
        last_digits: card last 4 digits
        bins: bins
    """
    try:
        times = []
        num_cores = int(mp.cpu_count() * 1.5)
        
        for i in tqdm(range(1, num_cores + 1), desc='Finding collisions'):
            start_time = time.time()
            with mp.Pool(i) as pool:
                results = pool.starmap(check_number_card, [(j, hash, last_digits, bins) for j in range(1000000)])
                for result in results:
                    if result is not None:
                        break
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)
        
        plt.plot(range(1, num_cores + 1), times, color="green", marker="o", markersize=7)
        plt.xlabel("Amount of processes")
        plt.ylabel("Time in seconds")
        plt.title("Dependence of time to find collision from amount of processes")
        plt.show()
    except Exception as ex:
        logging.error(ex)
