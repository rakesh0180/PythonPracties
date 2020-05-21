class TagCloud:
    def __init__(self):
        self.__tags = {

        }

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __len__(self):
        return len(self.__tags)

    def __getitem__(self, tag):
        return self.__tags.get(tag, 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __iter__(self):
        return iter(self.__tags)


could = TagCloud()
could["python"] = 10
could.add("pythp")
could.add("pythp")
could.add("Pythp")
could.add("Pprythp")
print(could.__tags)
print("len", len(could.__tags))
for tag in could:
    print(tag)

print(could.__tags)
