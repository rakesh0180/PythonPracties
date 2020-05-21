num = int(input("enter end tabels\n"))
num1 = int(input("enter end tabels to cut"))
list = []
with open("table.doc", "w")as tables:
    for i in range(1, num+1):
        for j in range(1, num1 + 1):
            if j < 10:
                tables.write(f"{i} X 0{j} = {i*j}\n")
                # list.append(f"{i} X 0{j} = {i*j}")
                # tables.write(list)
                # tables.write(" ".join(f"{i} X 0{j}={i*j}"))

            else:
                # list.append(f"{i} X {j} = {i*j}")
                # tables.write(list)

                tables.write(f"{i} X {j} = {i*j}\n")
