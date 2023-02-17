# (*args)Unlimited Positional Arguments
def add(*args):
    # This is a tuple
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(2, 5, 10, 20)

# (**kwargs)Many Keyword Arguments


def calculate(n, **kwargs):
    # This is a Dictionary
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # Get method returns none when the argument don't pass
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
