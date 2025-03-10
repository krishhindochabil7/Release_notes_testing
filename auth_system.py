import hashlib

users = {
    "admin": hashlib.sha256("StrongP@ssw0rd!".encode()).hexdigest(),
    "user": hashlib.sha256("User$ecureP@ss".encode()).hexdigest()
}

def authenticate(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed_password:
        return "Access granted!"
    else:
        return "Access denied!"

# Usage Example
user_input = input("Enter username: ")
pass_input = input("Enter password: ")

print(authenticate(user_input, pass_input))
