import json
import logging
import pickle


class FileOperations:
    @staticmethod
    def read_text(path: str) -> str:
        try:
            with open(path, 'r', encoding='UTF-8') as f:
                text = f.read().lower()
            return text
        except FileNotFoundError:
            return "File with text for encryption not found"
        except Exception as e:
            logging.error(f'[reading_from_txt]: {e}')

    @staticmethod
    def read_json(file: str) -> dict:
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("File with settings not found")
            return {}
        except Exception as e:
            logging.error(f'[reading_from_json]: {e}')
            return {}
        return data

    @staticmethod
    def read_binary(path: str) -> bytes:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            return data
        except FileNotFoundError:
            return b"File not found"
        except Exception as e:
            logging.error(f'[reading_from_bin]: {e}')

    @staticmethod
    def read_encrypt(path: str) -> bytes:
        try:
            with open(path, 'rb') as f:
                data = pickle.load(f)
            return data
        except FileNotFoundError:
            return b"File not found"
        except Exception as e:
            logging.error(f'[reading_from_encrypt]: {e}')

    @staticmethod
    def write_text(path: str, text: str) -> None:
        try:
            with open(path, 'w', encoding='UTF-8') as f:
                f.write(text)
        except FileNotFoundError:
            print("Incorrect directory path")
        except Exception as e:
            logging.error(f'[writing_to_txt]: {e}')

    @staticmethod
    def write_binary(path: str, data: bytes) -> None:
        try:
            with open(path, 'wb') as f:
                f.write(data)
        except FileNotFoundError:
            print("Incorrect directory path")
        except Exception as e:
            logging.error(f'[writing_to_bin]: {e}')

    @staticmethod
    def write_encrypt(path: str, data: bytes) -> None:
        try:
            with open(path, 'wb') as f:
                pickle.dump(data, f)
        except FileNotFoundError:
            print("Incorrect directory path")
        except Exception as e:
            logging.error(f'[writing_to_encrypt]: {e}')

    @staticmethod
    def write_decrypt(path: str, data: bytes) -> None:
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(data.decode('utf-8'))
        except FileNotFoundError:
            print("Incorrect directory path")
        except Exception as e:
            logging.error(f'[writing_to_decrypt]: {e}')
