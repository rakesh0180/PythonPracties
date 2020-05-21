# unpacking list
letters = ["a", "b", "c", "d"]
first, second, thrid, fourth = letters
# first, second, thrid = letters
# the above line show error because the list have 4 elements but we
# declared 3 variables
print(first)
print(second)
print(thrid)
print(fourth)

print("\n\nunpacking")
first, second, *others = letters
print(first)
print(second)
print(others)

print("\n\nunpacking")
first, *others = letters
print(first)
print(others)
