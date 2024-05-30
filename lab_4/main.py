import os
import json
import logging
import argparse

from functions import number_search, luna_algorithm, collision_dependence


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--options', type=str, default=os.path.join('lab_4', 'options.json'),
                        help='Path to the options file')
    args = parser.parse_args()

    try:
        with open(args.options, 'r') as file:
            options = json.load(file)

        bins = options.get("bins")
        hash_value = options.get("hash")
        last_digits = options.get("digits_last")
        save_path = options.get("path")

        if not bins or not hash_value or not last_digits or not save_path:
            logging.error("Invalid settings file.")
            exit(1)

        result = number_search(save_path, hash_value, last_digits, bins)
        
        if result:
            if luna_algorithm(result):
                logging.info("The card number is valid according to the Luhn algorithm.")
            else:
                logging.info("The card number is invalid according to the Luhn algorithm.")
        
        collision_dependence(hash_value, last_digits, bins)

    except Exception as ex:
        logging.error(f"An error occurred: {ex}")
