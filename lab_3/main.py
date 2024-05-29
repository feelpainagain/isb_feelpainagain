from functions import *


def main():
    parser = argparse.ArgumentParser(description='main.py')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', type=str, help='Call function to generate keys', dest='generation')
    group.add_argument('-enc', '--encryption', type=str, help='Call function to encrypt', dest='encryption')
    group.add_argument('-dec', '--decryption', type=str, help='Call function to decrypt', dest='decryption')
    parser.add_argument("-isec", "--input_secret_key", dest="secret_key", default="files/keys/secret_key.pem",
                        required=False, type=validate_file, help="input path to secret key", metavar="FILE")
    parser.add_argument("-ipk", "--input_public_key", dest="public_key", default="files/keys/public_key.pem",
                        required=False, type=validate_file, help="input path to public key", metavar="FILE")
    parser.add_argument("-isym", "--input_symmetric_key", dest="symmetric_key", default="files/keys/symmetric_key.txt",
                        required=False, type=validate_file, help="input path to symmetric key", metavar="FILE")
    parser.add_argument("-ipl", "--input_plain_text", dest="plain_text", default="files/texts/text.txt",
                        required=False, type=validate_file, help="input path to plain text", metavar="FILE")
    parser.add_argument("-ienc", "--input_encrypted_text", dest="encrypted_text",
                        default="files/texts/encrypted_text.txt", required=False, type=validate_file,
                        help="input path to encrypted text", metavar="FILE")
    parser.add_argument("-idec", "--input_decrypted_text", dest="decrypted_text",
                        default="files/texts/decrypted_text.txt", required=False, type=validate_file,
                        help="input path to decrypted text", metavar="FILE")
    args = parser.parse_args()

    (value, path_symmetric_key, path_public_key, path_secret_key,
     path_initial_file, path_encrypted_file, path_decrypted_file) = get_arguments(args, "settings.json")

    match value:
        case 'generation':
            key_generation(path_symmetric_key, path_public_key, path_secret_key)
            print('keys created')
        case 'encryption':
            encrypt_file(path_initial_file, path_secret_key, path_symmetric_key, path_encrypted_file)
            print('file encrypted')
        case 'decryption':
            decrypt_file(path_encrypted_file, path_secret_key, path_symmetric_key, path_decrypted_file)
            print('file decrypted')
        case _:
            print(f"Args '{args}' not understood")


if __name__ == "__main__":
    main()
