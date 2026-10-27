from functools import wraps


def show_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Calculator:
    @show_call
    def multiply(self, a, b):
        return a * b


calculator = Calculator()
print("Result:", calculator.multiply(9, 8))
