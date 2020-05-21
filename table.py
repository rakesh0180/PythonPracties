print("enter number to print multiply")
number1 = int(input(">"))
print("enter number to last stop")
number2 = int(input(">"))
count = 1
for i in range(1, number2):
    if (count <= number2):
        print(f"{number1} x {count} =", number1 * count)
        count += 1
        print(number1, "x", i, "=", number1*i)
