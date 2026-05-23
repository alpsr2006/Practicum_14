text = input()
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Сортировка по частоте (убывание)
items = list(freq.items())
for i in range(len(items)):
    for j in range(len(items) - 1):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

result = [word for word, _ in items]
print(" ".join(result))