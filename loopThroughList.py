letters = ["a", "b", "c", "d"]
for letter in letters:
    print(letter)


# iterate using enum for index
for letter in enumerate(letters):
    print(letter)
for letter in enumerate(letters):
    print("index", letter[0])
for letter in enumerate(letters):
    print("value", letter[1])
for letter in enumerate(letters):
    print("index={0}, value={1}".format(letter[0], letter[1]))


# iterate using unpacking
# it use tuples
# for indexing
for index, letter in enumerate(letters):
    print(index, letter)

