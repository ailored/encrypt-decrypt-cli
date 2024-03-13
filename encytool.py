from Crypto.Cipher import AES
from base64 import b64encode
import argparse
import sys


def encrypt_data(key: bytes, bytes_text: bytes, path_to_savefile: str) -> tuple[bytes, bytes, bytes]:
    cipher = AES.new(key=key, mode=AES.MODE_GCM, mac_len=16)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plaintext=bytes_text)

    with open(path_to_savefile, 'wb') as encrypted_file:
        encrypted_file.write(nonce + tag + ciphertext)

    return nonce, ciphertext, tag


def decrypt_data(key: bytes, encryptedfile_path: str) -> tuple[str, bytes, bytes]:
    with open(encryptedfile_path, 'rb') as encrypted_file:
        nonce: bytes = encrypted_file.read(16)
        tag: bytes = encrypted_file.read(16)
        ciphertext: bytes = encrypted_file.read()

    cipher = AES.new(key=key, mode=AES.MODE_GCM, nonce=nonce, mac_len=16)
    original_text: str = cipher.decrypt_and_verify(ciphertext=ciphertext, received_mac_tag=tag).decode()
    return original_text, tag, nonce


def parse_arguments() -> tuple[str, str, str]:
    parser = argparse.ArgumentParser(description='CLI encryption-decryption tool based on AES encryption algorithm')
    parser.add_argument('-e', '--encrypt', action='store_true', help='specify it if you want to encrypt the data')
    parser.add_argument('-d', '--decrypt', action='store_true', help='specify it if you want to decrypt the data')
    parser.add_argument('keyfile_path', action='store', help='specify location of the binary encryption key file')
    args = parser.parse_args()

    if not args.encrypt and not args.decrypt:
        parser.error('please specify either --encrypt or --decrypt')

    return args.encrypt, args.decrypt, args.keyfile_path


def read_keyfile(key_path: str) -> bytes:
    with open(key_path, 'rb') as key_file:
        key: bytes = key_file.read()
    return key


def get_data_to_encrypt() -> bytes:
    specified_data: list[str] = sys.stdin.readlines()
    bytes_data: bytes = b' '.join(s.encode('utf-8') for s in specified_data)

    return bytes_data


def main():
    is_encoding, is_decoding, path = parse_arguments()
    key: bytes = read_keyfile(path)

    if is_encoding:
        original_data: bytes = get_data_to_encrypt()
        nonce, ciphered_text, mac_tag = encrypt_data(key=key, bytes_text=original_data,
                                                     path_to_savefile='data/encrypted_data.bin')

        # sys.stdout.write(f'CIPHERTEXT={b64encode(ciphered_text).decode("utf-8")}\n')
        sys.stdout.write(f'NONCE={b64encode(nonce).decode("utf-8")}\n')
        sys.stdout.write(f'MAC-TAG={b64encode(mac_tag).decode("utf-8")}\n')

    if is_decoding:
        decrypted_data, dec_tag, dec_nonce = decrypt_data(key=key, encryptedfile_path='data/encrypted_data.bin')

        # sys.stdout.write(f'DECRYPTED ORIGINAL DATA={decrypted_data}\n')
        sys.stdout.write(f'RECEIVED NONCE={b64encode(dec_nonce).decode("utf-8")}\n')
        sys.stdout.write(f'RECEIVED MAC-TAG={b64encode(dec_tag).decode("utf-8")}\n')


if __name__ == '__main__':
    main()
