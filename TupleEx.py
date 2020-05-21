items = [
    ("p1", 4),
    ("p2", 2),
    ("p3", 5)

]


# def sort_item(item):
#     return item[1]


# print(item.sort(key=sort_item))
# print(item)
# using lambada we avoid above two statement
items.sort(key=lambda item: item[1])
print(items)

# map
x = list(map(lambda item: item[1], items))
print("map", x)

# filter
y = list(filter(lambda item: item[1] >= 3, items))
print("filter", y)

# list comphersion
# it is used inside of lambda

filter = [item[1] for item in items]
print("filter", filter)
