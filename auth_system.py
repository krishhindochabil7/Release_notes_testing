import getpass
import hashlib

# User database (stores username: hashed password)
users = {
    "admin": hashlib.sha256("StrongP@ssw0rd!".encode()).hexdigest(),
    "user": hashlib.sha256("User$ecureP@ss".encode()).hexdigest()
}

# Tracks failed login attempts
failed_attempts = {}

def hash_password(password):
    """Returns SHA-256 hashed password."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    """Authenticates a user based on username and password."""
    username = username.lower()  # Make usernames case-insensitive

    if username in failed_attempts and failed_attempts[username] >= 3:
        return "Too many failed attempts. Try again later."

    hashed_password = hash_password(password)
    if username in users and users[username] == hashed_password:
        failed_attempts[username] = 0  # Reset failed attempts on success
        return "Access granted!"
    else:
        failed_attempts[username] = failed_attempts.get(username, 0) + 1
        return "Access denied!"

def register_user(username, password):
    """Registers a new user with a hashed password."""
    username = username.lower()
    if username in users:
        return "User already exists!"
    
    users[username] = hash_password(password)
    return "User registered successfully!"

# Main logic
choice = input("Do you want to (L)ogin or (R)egister? ").strip().lower()

if choice == "r":
    new_user = input("Enter new username: ").strip()
    new_pass = getpass.getpass("Enter new password: ")
    print(register_user(new_user, new_pass))
else:
    user_input = input("Enter username: ").strip()
    pass_input = getpass.getpass("Enter password: ")
    print(authenticate(user_input, pass_input))
