# list example
numbers = [1, 2, 3, 4]
print(numbers[0], numbers[1])
first, second, third, fourth = numbers
print(first)
print(second)
print(third)
print(fourth)

a, b, *c = numbers
print(a)
print(b)
print(c)
"""what i need if i get last item in a list

"""
a, *other, c = numbers
print(a, c)
print(other)
