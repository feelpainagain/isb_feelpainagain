from work_files import FileOperations


class ArgumentParser:
    def __init__(self):
        self.file_ops = FileOperations()

    def get_arguments(self, args, path_to_settings: str):
        json_data = self.file_ops.read_json(path_to_settings)

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
