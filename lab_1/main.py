from work_files import *
from consts import *


def task_1(plain_text: str, key: str, encrypted: str):
    """ simple transposition cipher encryption
    Args:
      plain_text: encrypted text
      key: required key (string)
      encrypted: string with result cipher
    """
    text = read_text(plain_text)
    alphabet_replacement = read_text(key)

    print(alphabet_replacement)

    result_string = encrypt(text, alphabet_replacement)

    print(result_string)

    write_text(encrypted, result_string)

    for i in range(0, len(ALPHABET)):
        print(ALPHABET[i] + ' -> ' + alphabet_replacement[i])


def task_2(plain_text: str, key: str, decrypted: str, normal_alphabet: str):
    """ func for decryption
    Args:
      plain_text: encrypted text
      key: required key (string)
      decrypted: string with result cipher
      normal_alphabet: alphabet for decryption
    """
    crypt_alphabet = read_text(key)
    normal_alphabet = read_text(normal_alphabet)

    decryption_mapping = dict(zip(crypt_alphabet, normal_alphabet))

    data = read_text(plain_text)

    decrypted_text = decrypt(data, decryption_mapping)

    write_text(decrypted, decrypted_text)


def main():
    text_1, key_1, encrypted, text_2, key_2, \
        decrypted, normal_alphabet = read_json("paths.json")
    task_1(text_1, key_1, encrypted)
    task_2(text_2, key_2, decrypted, normal_alphabet)


if __name__ == '__main__':
    main()
