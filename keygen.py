from Crypto import Random


def generate_key(key_size: int) -> bytes:
    return Random.get_random_bytes(key_size)


def save_key_to_file(key: bytes, filename: str):
    with open(filename, 'wb') as key_file:
        key_file.write(key)


def main():
    key_size: int = 16
    keyfile_location: str = 'key/encryption_key.bin'

    key: bytes = generate_key(key_size)
    save_key_to_file(key=key, filename=keyfile_location)


if __name__ == '__main__':
    main()
