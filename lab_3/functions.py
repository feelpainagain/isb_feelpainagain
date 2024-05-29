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
    json_data = read_json(path_to_settings)

    value = ''
    path_symmetric_key = ''
    path_public_key = ''
    path_secret_key = ''
    path_initial_file = ''
    path_encrypted_file = ''
    path_decrypted_file = ''

    if args.generation is not None:
        value = 'generation'
        if args.symmetric_key is not None:
            path_symmetric_key = args.symmetric_key
        if args.public_key is not None:
            path_public_key = args.public_key
        if args.secret_key is not None:
            path_secret_key = args.secret_key
    elif args.encryption is not None:
        value = 'encryption'
        if args.symmetric_key is not None:
            path_symmetric_key = args.symmetric_key
        if args.public_key is not None:
            path_public_key = args.public_key
        if args.secret_key is not None:
            path_secret_key = args.secret_key
        if args.plain_text is not None:
            path_initial_file = args.plain_text
        if args.encrypted_text is not None:
            path_encrypted_file = args.encrypted_text
    elif args.decryption is not None:
        value = 'decryption'
        if args.symmetric_key is not None:
            path_symmetric_key = args.symmetric_key
        if args.public_key is not None:
            path_public_key = args.public_key
        if args.secret_key is not None:
            path_secret_key = args.secret_key
        if args.encrypted_text is not None:
            path_encrypted_file = args.encrypted_text
        if args.decrypted_text is not None:
            path_decrypted_file = args.decrypted_text

    return (value, path_symmetric_key, path_public_key, path_secret_key, path_initial_file,
            path_encrypted_file, path_decrypted_file)
