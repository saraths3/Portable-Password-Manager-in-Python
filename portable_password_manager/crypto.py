from cryptography.fernet import Fernet

def load_key():
    try: return open("secret.key", "rb").read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        open("secret.key", "wb").write(key)
        return key

key = load_key()
cipher_suite = Fernet(key)