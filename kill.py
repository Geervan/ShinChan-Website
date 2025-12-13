import os
import json

def get_user_data(username):
    # SECURITY: Path traversal vulnerability!
    # User can pass "../../../etc/passwd" as username
    file_path = f"users/{username}.json"
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def update_password(username, new_password):
    # LOGIC BUG: Using '==' for assignment instead of '='
    user = get_user_data(username)
    if user:
        user['password'] == new_password  # Bug! This does nothing.
        save_user(user) # Assume this exists
        return True
    return False
