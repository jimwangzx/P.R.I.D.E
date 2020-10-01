import pyotp
from app import *

def generate_totp(base32_secret_key):
    totp=pyotp.TOTP(base32_secret_key)
    totp_live=totp.now()
    return totp_live

def generate_secret_totp_key():
    totp_key=pyotp.random_base32()
    return totp_key

