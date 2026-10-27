from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing function...")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def calculate_square(number):
    """Return the square of a number."""
    return number ** 2


print(calculate_square(5))
print(calculate_square.__name__)
print(calculate_square.__doc__)
