
def greet(name):
    print(f"hi {name}")


greet("Raki")
print(greet("muni"))

# argument
print("argument")


def add(num1, numb2):
    return num1 + numb2


a = add(2, 2)
print(add(3, 3))
print(a)

# default argument
print("default argument")


def addition(num, by):
    num += by


addition(4, 5)


def addition1(num, by=5):
    num += by


addition(4, 5)


# xargs
print("xargs")


def mulitiply(*numbers):
    total = 1
    print("Mulitiplication")
    print("tuples", numbers)
    for number in numbers:
        print(number)
        total *= number
    return total


print(mulitiply(2, 3, 4, 5, 6))

# xxargs
print("xxargs")


def fruit_quality(**fruits):
    print(fruits)
    print("accessing elements", fruits["apple"])


fruit_quality(apple=4, orange=3, grapes=10)
