import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt", "r") as f:
        passwords = [line.strip() for line in f]

    salts = []
    if use_salts:
        with open("known-salts.txt", "r") as f:
            salts = [line.strip() for line in f]

    if use_salts:
        for password in passwords:
            for salt in salts:
                if hashlib.sha1((salt + password).encode()).hexdigest() == hash:
                    return password
                if hashlib.sha1((password + salt).encode()).hexdigest() == hash:
                    return password
    else:
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password

    return "PASSWORD NOT IN DATABASE"