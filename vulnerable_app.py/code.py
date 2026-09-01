username = input("Enter username: ")
password = input("Enter password: ")

users = {
    "admin": "admin123",
    "user": "password123"
}

if username in users:
    if users[username] == password:
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Username not found")