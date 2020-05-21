sentence = "this is a common interview  question"
char_frequence = {}
for char in sentence:
    if char in char_frequence:
        char_frequence[char] += 1
    else:
        char_frequence[char] = 1

print(char_frequence)

char_frequence_sorted = sorted(
    char_frequence.items(), key=lambda ky: ky[1], reverse=True)
print(char_frequence_sorted[0])
