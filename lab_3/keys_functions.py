import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from work_files import FileOperations


class KeyManagement:
    def __init__(self):
        self.file_ops = FileOperations()

    def key_generation(self, path_to_symmetric_key: str, path_to_public_key: str, path_to_secret_key: str) -> None:
        symmetric_key = os.urandom(128 // 8)

        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_k = keys

        private_pem = private_k.private_bytes(encoding=serialization.Encoding.PEM,
                                              format=serialization.PrivateFormat.TraditionalOpenSSL,
                                              encryption_algorithm=serialization.NoEncryption())
        self.file_ops.write_binary(path_to_secret_key, private_pem)

        public_k = keys.public_key()
        public_pem = public_k.public_bytes(encoding=serialization.Encoding.PEM,
                                           format=serialization.PublicFormat.SubjectPublicKeyInfo)
        self.file_ops.write_binary(path_to_public_key, public_pem)

        enc_symmetrical_key = public_k.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                           algorithm=hashes.SHA256(), label=None))
        self.file_ops.write_binary(path_to_symmetric_key, enc_symmetrical_key)

    def decrypt_symmetric_key(self, path_to_symmetric_key: str, path_to_secret_key: str) -> bytes:
        enc_symmetrical_key = self.file_ops.read_binary(path_to_symmetric_key)
        private_k = self.file_ops.read_binary(path_to_secret_key)
        private_k = serialization.load_pem_private_key(private_k, password=None)
        symmetrical_key = private_k.decrypt(enc_symmetrical_key,
                                            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                         algorithm=hashes.SHA256(), label=None))
        return symmetrical_key
