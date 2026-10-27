def log_function(func):
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("Arguments:", args)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper


@log_function
def add(a, b):
    return a + b


add(30, 40)
