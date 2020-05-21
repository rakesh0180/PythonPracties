'''a = "i am rakesh"
for b in range(0, len(a)):
    print(a[b])'''

list = [9, 7, 1, 2, 3, 4, 5]
list.sort()
print(list)  # [1, 2, 3, 4, 5, 7, 9]

list1 = list.copy()
print("list1", list1)  # list1 [1, 2, 3, 4, 5, 7, 9]
print(list.index(1))  # 0
list.remove(3)
print(list)  # [1, 2, 4, 5, 7, 9]
list.insert(2, 3)
print(list)  # [1, 2, 3, 4, 5, 7, 9]
list.append(4)
print(list)  # [1, 2, 3, 4, 5, 7, 9,4]
list.pop()
print("pop", list)  # [1, 2, 3, 4, 5, 7, 9] 4 is removed
list.pop(4)
print("pop", list)  # [1, 2, 3, 4, 7, 9]
list.reverse()
print("reverse", list)  # reverse [9, 7, 4, 3, 2, 1]
list.clear()
print(list)
