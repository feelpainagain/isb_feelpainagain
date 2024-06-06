import argparse
import json

from parser import ArgumentParser
from functions import EncryptionManagement
from keys_functions import KeyManagement


def load_settings(settings_path):
    with open(settings_path, 'r') as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(description="Encryption and Decryption")
    parser.add_argument('--generation', action='store_true', help="Generate keys")
    parser.add_argument('--encryption', action='store_true', help="Encrypt file")
    parser.add_argument('--decryption', action='store_true', help="Decrypt file")
    parser.add_argument('--symmetric_key', type=str, help="Path to symmetric key")
    parser.add_argument('--public_key', type=str, help="Path to public key")
    parser.add_argument('--secret_key', type=str, help="Path to secret key")
    parser.add_argument('--plain_text', type=str, help="Path to initial file")
    parser.add_argument('--encrypted_text', type=str, help="Path to encrypted file")
    parser.add_argument('--decrypted_text', type=str, help="Path to decrypted file")
    parser.add_argument('--settings', type=str, default='settings.json', help="Path to settings file")

    args = parser.parse_args()

    # Load settings from the file
    settings = load_settings(args.settings)

    # Override settings with command line arguments if provided
    path_symmetric_key = args.symmetric_key or settings.get('symmetric_key')
    path_public_key = args.public_key or settings.get('public_key')
    path_secret_key = args.secret_key or settings.get('secret_key')
    path_initial_file = args.plain_text or settings.get('text')
    path_encrypted_file = args.encrypted_text or settings.get('encrypted_text')
    path_decrypted_file = args.decrypted_text or settings.get('decrypted_text')

    arg_parser = ArgumentParser()
    enc_mgmt = EncryptionManagement()
    key_mgmt = KeyManagement()

    if args.generation:
        key_mgmt.key_generation(path_symmetric_key, path_public_key, path_secret_key)
    elif args.encryption:
        enc_mgmt.encrypt_file(path_initial_file, path_secret_key, path_symmetric_key, path_encrypted_file)
    elif args.decryption:
        enc_mgmt.decrypt_file(path_encrypted_file, path_secret_key, path_symmetric_key, path_decrypted_file)


if __name__ == "__main__":
    main()
