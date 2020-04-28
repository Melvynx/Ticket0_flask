# key.py
# MM 2020
# file with list of key
from cryptography.fernet import Fernet

cookie_key = "8ziuwcKuIkVSApIlb4G2CK6m9X9aR_UKLGdMhk8_R9Y="

fernet_cookie = Fernet(cookie_key)


def encrypt(text):
    return fernet_cookie.encrypt(text.encode()).decode("utf-8")


def decrypt(token):
    return fernet_cookie.decrypt(token.encode()).decode("utf-8")
