from cryptography.fernet import Fernet
from app import *

'''
key=Fernet.generate_key()
file=open("key.key","wb")
file.write(key)
file.close()
'''

def get_key():
    file=open("key.key","rb")
    key=file.read()
    return key

def init_fernet(key):
    f=Fernet(key)
    return f

def encrypt(data):
    key=get_key()
    data=data.encode()
    f=init_fernet(key)
    encrypted_data=f.encrypt(data)
    return encrypted_data

def decrypt(data):
    key=get_key()
    f=init_fernet(key)
    decrypted_data=f.decrypt(data)
    data=decrypted_data.decode()
    return data
