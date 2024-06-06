from keys_functions import KeyManagement
from crypt_asymmetric import CryptoOperations
from work_files import FileOperations


class EncryptionManagement:
    def __init__(self):
        self.key_mgmt = KeyManagement()
        self.file_ops = FileOperations()
        self.crypto_ops = CryptoOperations()

    def encrypt_file(self, path_to_initial_file: str, path_to_secret_key: str, path_to_symmetric_key: str,
                     path_to_encrypt_file: str) -> None:
        symmetrical_key = self.key_mgmt.decrypt_symmetric_key(path_to_symmetric_key, path_to_secret_key)
        txt = self.file_ops.read_binary(path_to_initial_file)
        res = self.crypto_ops.encrypt(txt, symmetrical_key)
        self.file_ops.write_encrypt(path_to_encrypt_file, res)

    def decrypt_file(self, path_to_encrypt_file: str, path_to_secret_key: str, path_to_symmetric_key: str,
                     path_to_decrypted_file: str) -> None:
        symmetrical_key = self.key_mgmt.decrypt_symmetric_key(path_to_symmetric_key, path_to_secret_key)
        cipher_tmp = self.file_ops.read_encrypt(path_to_encrypt_file)
        cipher_txt = cipher_tmp['ciphertxt']
        iv = cipher_tmp['iv']
        dec_txt = self.crypto_ops.decrypt(cipher_txt, symmetrical_key, iv)
        self.file_ops.write_decrypt(path_to_decrypted_file, dec_txt)
