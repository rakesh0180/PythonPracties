try:
    a = int(input("Age : "))

except ValueError:
    print("only integers")

else:
    print("your age is = ", a)

# detail about the error
try:
    a = int(input("Age : "))
    pass
except ValueError as ex:
    print(ex)
    print(type(ex))
    pass

# multiple exception
try:
    a = int(input("age : "))
    c = 20/a
    pass
except (ValueError, ZeroDivisionError):
    print("enter only integer and it must > 0")
    pass

#raise exception
age = 2
if (age >= 0):
    raise ValueError("integers only")
