import random
import hashlib
from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# f = Fernet(key)
# token = f.encrypt(b"Hello brother")
# print(token)

string = "hello hosyn"
enc = string.encode()
hash_ = hashlib.sha256(string=enc)
dec = hash_.hexdigest()
print(dec)

# while True:
#     rand = random.randint(0, 115792089237316195423570985008687907853269984665640564039457584007913129639935)
#     new = "{:064X}".format(rand)
#     print(new)
