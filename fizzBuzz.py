def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 == 0):
        return "Fizz"
    elif (input % 5 == 0):

        return "Buzz"
    else:
        return input


def fizz_buzz1(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"
    return input


print("start")
print(fizz_buzz(7))
