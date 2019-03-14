import hashlib

h = hashlib.sha1(b"password")
h = hashlib.sha1()
h.update(b"password")

h = hashlib.sha1(b"password")
h.digest()
print(h.hexdigest())
