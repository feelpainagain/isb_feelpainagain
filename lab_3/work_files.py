import argparse
import json
import logging
import os
import pickle


def read_text(path: str):
    """
    func that reads text from file
    Args:
      path: file path
    Returns:
      text from file
    """
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            text = f.read().lower()
        return text
    except FileNotFoundError:
        return "File with text for encryption not found"
    except Exception as e:
        logging.error(f'[reading_from_txt]: {e}')


def read_json(file: str):
    """
    func that reads json from file
    Args:
      file: file path
    Returns:
      parameters from json
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File with settings not found")
        return
    except Exception as e:
        logging.error(f'[reading_from_json]: {e}')
        return

    return data


def read_binary(path: str):
    """
    func that reads binary from file
    Args:
      path: file path
    Returns:
      data from file
    """
    try:
        with open(path, 'rb') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        logging.error(f'[reading_from_bin]: {e}')


def read_encrypt(path: str):
    """
    func that reads encrypted data from file
    Args:
      path: file path
    Returns:
      data from file
    """
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        logging.error(f'[reading_from_encrypt]: {e}')


def write_text(path: str, text: str):
    """
    func that whites info into file
    Args:
      path: file path
      text: text that is written
    """
    try:
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(text)
    except FileNotFoundError:
        print("Incorrect directory path")
    except Exception as e:
        logging.error(f'[writing_to_txt]: {e}')


def write_binary(path: str, data):
    """
    func that writes binary data to file
    Args:
      path: file path
      data: written data
    """
    try:
        with open(path, 'wb') as f:
            f.write(data)
    except FileNotFoundError:
        print("Incorrect directory path")
    except Exception as e:
        logging.error(f'[writing_to_bin]: {e}')


def write_encrypt(path: str, data):
    """
    func that writes encrypted data to file
    Args:
      path: file path
      data: written encrypt data
    """
    try:
        with open(path, 'wb') as f:
            pickle.dump(data, f)
    except FileNotFoundError:
        print("Incorrect directory path")
    except Exception as e:
        logging.error(f'[writing_to_encrypt]: {e}')


def write_decrypt(path: str, data):
    """
    func that writes decrypted data to file
    Args:
      path: file path
      data: written data
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data.decode('utf-8'))
    except FileNotFoundError:
        print("Incorrect directory path")
    except Exception as e:
        logging.error(f'[writing_to_decrypt]: {e}')


def validate_file(file):
    """
    func that checks is there a file or not
    Args:
        file: file path
    Returns:
        path to file (if exists)
    """
    if not os.path.exists(file):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(file))
    return file
