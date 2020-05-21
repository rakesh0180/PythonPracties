point = dict(x=1, y=2, z=3)

print(point)
point['x'] = 20
print(point)
# point['a'] # error
if "a" in point:
    print("a", point["a"])

print(point.get("a"))  # none
print(point.get("a", 0))  # if a is not exits print 0

for i in point:
    print(i, point[i])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)
value = {}
for x in range(5):
    value[x] = x * 2

print(value)

values = {x: x * 2 for x in range(5)}
print(values)
