word = input()
words = []

for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        words.append(part1 + part2 + part3)

print(sorted(words)[0])