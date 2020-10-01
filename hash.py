from app import *

def getip():
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    return ip

def getsalt(password):
    salt_used=password[21:43]
    salt_decoded=passlib.utils.binary.ab64_decode(salt_used)
    return salt_decoded

def get_user_cred(given_salt, given_pass):
    ip=getip()
    user_pass=str(ip)+given_pass
    hash=pbkdf2_sha256.using(salt=given_salt).hash(user_pass)
    return hash
