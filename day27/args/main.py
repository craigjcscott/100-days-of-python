def add(*args):
    return sum(args)


def calculate(n, **kwargs):
    if "add" in kwargs:
        n += kwargs["add"]
    if "multiply" in kwargs:
        n *= kwargs["multiply"]
    return n


print(add(1, 2, 3, 4))
print(calculate(2, add=3, subtract=10))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")  # get() works like a square bracket, but no error if missing


my_car = Car(make="Subaru")
print(my_car.model)

