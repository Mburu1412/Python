import hashlib
import os
import secrets

class User:
    def __init__(self, username, password_hash, salt):
        self.username = username
        self.password_hash = password_hash
        self.salt = salt

    def get_username(self):
        return self.username

    def get_password_hash(self):
        return self.password_hash

    def get_salt(self):
        return self.salt

class PasswordSecurity:
    def __init__(self, minimum_length=8):
        self.minimum_length = minimum_length

    def is_strong_password(self, password):
        if len(password) < self.minimum_length:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        return True

    def generate_salt(self):
        return secrets.token_hex(16) # 16 bytes = 32 hex characters

    def hash_password(self, password, salt):
         salted_password = salt.encode() + password.encode()
         hashed_password = hashlib.sha256(salted_password).hexdigest()
         return hashed_password


class AuthenticationSystem:
    def __init__(self, password_security):
        self.users = {}
        self.password_security = password_security

    def register_user(self, username, password):
        if username in self.users:
            return "Error: Username already exists."

        if not self.password_security.is_strong_password(password):
            return "Error: Password does not meet strength requirements."

        salt = self.password_security.generate_salt()
        password_hash = self.password_security.hash_password(password, salt)
        user = User(username, password_hash, salt)
        self.users[username] = user
        return "User registered successfully."

    def authenticate_user(self, username, password):
        if username not in self.users:
            return "Authentication failed: Invalid username."

        user = self.users[username]
        salt = user.get_salt()
        hashed_password = self.password_security.hash_password(password, salt)

        if hashed_password == user.get_password_hash():
            return "Authentication successful."
        else:
            return "Authentication failed: Incorrect password."


# Example Usage
password_security = PasswordSecurity()
auth_system = AuthenticationSystem(password_security)

# Registration
registration_result = auth_system.register_user("testuser", "P@ssword123")
print(registration_result)

# Authentication
authentication_result = auth_system.authenticate_user("testuser", "P@ssword123")
print(authentication_result)

authentication_result = auth_system.authenticate_user("testuser", "wrongpassword")
print(authentication_result)
