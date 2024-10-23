from passlib.context import CryptContext

crypt_contex = CryptContext(schemes=['bcrypt'])


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return crypt_contex.verify(plain_password, hashed_password)


def generate_password_hash(password: str) -> str:
    return crypt_contex.hash(password)
