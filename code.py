# Dummy login system

# Predefined username and password
stored_username = "user123"
stored_password = "pass123"

# Ask user for input
input_username = input("Enter username: ")
input_password = input("Enter password: ")

# Check if the input matches
if input_username == stored_username and input_password == stored_password:
    print("Login successful!")
else:
    print("Login failed. Incorrect username or password.")
