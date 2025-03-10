users = {
    "admin": "password123",  # Weak hardcoded password
    "user": "12345"
}

def authenticate(username, password):
    if username in users and users[username] == password:
        return "Access granted!"
    else:
        return "Access denied!"

# Usage Example
user_input = input("Enter username: ")
pass_input = input("Enter password: ")

print(authenticate(user_input, pass_input))
