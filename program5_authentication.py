from functools import wraps


def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in", False):
            print("Access denied! Please log in.")
            return None

        return func(user, *args, **kwargs)
    return wrapper


@require_login
def dashboard(user):
    print(f"Welcome, {user['name']}!")


user1 = {"name": "Sanjivani", "logged_in": True}
user2 = {"name": "khushi", "logged_in": True}

dashboard(user1)
dashboard(user2)
