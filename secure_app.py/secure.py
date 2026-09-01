import hashlib
import getpass

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

users = {
    "admin": hashlib.sha256("Admin@123".encode()).hexdigest(),
    "user": hashlib.sha256("User@123".encode()).hexdigest()
}

hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username in users and users[username] == hashed_password:
    print("Login successful")
else:
    print("Invalid username or password")