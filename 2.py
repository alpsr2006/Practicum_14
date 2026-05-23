n = int(input())

dictionary = {}
for _ in range(n):
    ru, en = input().split()
    dictionary[ru.lower()] = en

phrase = input()
words = phrase.split()

result = [dictionary.get(w, w) for w in words]
print(" ".join(result))