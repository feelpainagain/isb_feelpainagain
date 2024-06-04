from crypt_asymmetric import *
from keys_functions import *


def encrypt_file(path_to_initial_file: str, path_to_secret_key: str, path_to_symmetric_key: str,
                 path_to_encrypt_file: str) -> None:
    """
    :param path_to_initial_file: Path to text
    :param path_to_secret_key: Path to secret key
    :param path_to_symmetric_key: Path to symmetric key
    :param path_to_encrypt_file: Path to encrypted file
    """
    symmetrical_key = decrypt_symmetric_key(path_to_symmetric_key, path_to_secret_key)
    txt = read_binary(path_to_initial_file)
    res = encrypt(txt, symmetrical_key)
    write_encrypt(path_to_encrypt_file, res)


def decrypt_file(path_to_encrypt_file: str, path_to_secret_key: str, path_to_symmetric_key: str,
                 path_to_decrypted_file: str) -> None:
    """
    :param path_to_encrypt_file: Path to encrypted file
    :param path_to_secret_key: Path to secret key
    :param path_to_symmetric_key: Path to symmetric key
    :param path_to_decrypted_file: Path to decrypted file
    """
    symmetrical_key = decrypt_symmetric_key(path_to_symmetric_key, path_to_secret_key)
    cipher_tmp = read_encrypt(path_to_encrypt_file)
    cipher_txt = cipher_tmp['ciphertxt']
    iv = cipher_tmp['iv']
    dec_txt = decrypt(cipher_txt, symmetrical_key, iv)
    write_decrypt(path_to_decrypted_file, dec_txt)


def get_arguments(args, path_to_settings):
    """
    func that obtains a set of arguments required for programme execution
        Args:
            args: set of arguments got from terminal
            path_to_settings: path to the settings file with default settings if the user has not entered args
        Returns:
            data required for program execution
        """
    json_data = read_json(path_to_settings)

    value = ''
    path_symmetric_key = ''
    path_public_key = ''
    path_secret_key = ''
    path_initial_file = ''
    path_encrypted_file = ''
    path_decrypted_file = ''

    match args:
        case args if args.generation:
            value = 'generation'
            match args:
                case args if args.symmetric_key and args.public_key and args.secret_key:
                    path_symmetric_key = args.symmetric_key
                    path_public_key = args.public_key
                    path_secret_key = args.secret_key
                case _:
                    path_symmetric_key = json_data["symmetric_key"]
                    path_public_key = json_data["public_key"]
                    path_secret_key = json_data["secret_key"]
        case args if args.encryption:
            value = 'encryption'
            match args:
                case args if (args.symmetric_key and args.public_key and args.secret_key
                              and args.plain_text and args.encrypted_text):
                    path_symmetric_key = args.symmetric_key
                    path_public_key = args.public_key
                    path_secret_key = args.secret_key
                    path_initial_file = args.plain_text
                    path_encrypted_file = args.encrypted_text
                case _:
                    path_symmetric_key = json_data["symmetric_key"]
                    path_public_key = json_data["public_key"]
                    path_secret_key = json_data["secret_key"]
                    path_initial_file = json_data["text"]
                    path_encrypted_file = json_data["encrypted_text"]
        case args if args.decryption:
            value = 'decryption'
            match args:
                case args if (args.symmetric_key and args.public_key and args.secret_key
                              and args.encrypted_text and args.decrypted_text):
                    path_symmetric_key = args.symmetric_key
                    path_public_key = args.public_key
                    path_secret_key = args.secret_key
                    path_encrypted_file = args.encrypted_text
                    path_decrypted_file = args.decrypted_text
                case _:
                    path_symmetric_key = json_data["symmetric_key"]
                    path_public_key = json_data["public_key"]
                    path_secret_key = json_data["secret_key"]
                    path_encrypted_file = json_data["encrypted_text"]
                    path_decrypted_file = json_data["decrypted_text"]
        case _:
            print(f"Args '{args}' not understood")

    return (value, path_symmetric_key, path_public_key, path_secret_key, path_initial_file,
            path_encrypted_file, path_decrypted_file)
