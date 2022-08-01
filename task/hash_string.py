import hashlib


def hash_string(string: str) -> str: 
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()


if __name__ == '__main__':
    print(hash_string('Python Bootcamp'))
