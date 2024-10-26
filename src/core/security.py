from hashlib import sha512


def verify_password(plain_password: str, hashed_password: str) -> bool:
    hash = sha512(plain_password.encode('UTF-8')).hexdigest()
    return hash == hashed_password


def generate_password_hash(password: str) -> str:
    return sha512(password.encode('UTF-8')).hexdigest()
