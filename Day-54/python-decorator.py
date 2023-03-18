import time


# Simple Python Decorator Functions

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")


# Without the @ syntactic sugar

def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()
