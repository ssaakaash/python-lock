import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random as CryptoRandom


class Encryption:

    def __init__(self, key):
        self.key = key

    def digest_key(self):
        """ Use SHA-256 over key to get a proper-sized AES key """
        key = self.key
        return SHA256.new(key).digest()

    def get_aes(self, IV):
        """ AES instance """
        return AES.new(self.digest_key(), AES.MODE_CBC, IV)

    def encrypt(self, secret):
        """ Encrypt a secret """

        IV = CryptoRandom.new().read(AES.block_size)
        aes = self.get_aes(IV)
        padding = AES.block_size - len(secret) % AES.block_size

        secret += bytes([padding]) * padding
        data = IV + aes.encrypt(secret)

        return base64.b64encode(data)

    def decrypt(self, enc_secret):
        """ Decrypt a secret """

        enc_secret = base64.b64decode(enc_secret)
        IV = enc_secret[:AES.block_size]
        aes = self.get_aes(IV)

        data = aes.decrypt(enc_secret[AES.block_size:])
        padding = data[-1]
        if data[-padding:] != bytes([padding]) * padding:
            raise ValueError("Invalid padding...")

        return data[:-padding]