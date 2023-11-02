def authenticate(func):
    def wrapper(username):
        return func(username)

    return wrapper


def admin_required(func):
    def wrapper(username):
        from main import load_user_data  # Import the function from main.py
        if username in load_user_data() and load_user_data()[username]['role'] == 'admin':
            return func(username)  # Pass 'username' as an argument
        else:
            print("Access denied. Admin role required.")
    return wrapper

