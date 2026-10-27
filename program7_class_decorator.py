from functools import update_wrapper


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 8
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.calls += 8
        print("Call number:", self.calls)
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    print(f"Hello, {name}!")


greet("Khushi")
greet("Priya")
greet("Priya")
