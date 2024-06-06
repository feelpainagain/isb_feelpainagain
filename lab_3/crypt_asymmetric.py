import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class CryptoOperations:
    @staticmethod
    def encrypt(txt: bytes, symmetrical_key: bytes) -> dict:
        """
        func that encrypts txt using symmetrical key
        :param txt: text
        :param symmetrical_key: symmetric key
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.SEED(symmetrical_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_text = padder.update(txt) + padder.finalize()
        ciphertext = encryptor.update(padded_text) + encryptor.finalize()
        res = {'ciphertxt': ciphertext, 'iv': iv}

        return res

    @staticmethod
    def decrypt(cipher_txt: bytes, symmetrical_key: bytes, iv: bytes) -> bytes:
        """
        func that decrypts cipher txt using symmetrical key
        :param cipher_txt: encrypted text
        :param symmetrical_key: symmetric key
        :param iv: iv for decrypt
        """
        cipher = Cipher(algorithms.SEED(symmetrical_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(cipher_txt) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        dec_txt = unpadder.update(plaintext) + unpadder.finalize()

        return dec_txt
