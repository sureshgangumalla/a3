import hashlib


class PasswordHasher:

    def __init__(self):
        self.salt = '0bff061b49bf4c4f93dca1c761286bdd'

    def hash(self, password):
        hashed_password = self.salt + password
        hashed_password = hashed_password.encode('utf-8')
        hashed_password = hashlib.sha512(hashed_password).hexdigest()
        hashed_password = hashed_password[0:50]
        return hashed_password
