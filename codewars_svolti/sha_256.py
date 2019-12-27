import hashlib
def to_sha256(s):
    s = s.encode('utf-8')
    return hashlib.sha256(s).hexdigest()

print(funzione_sha_256("Hello World!"))
