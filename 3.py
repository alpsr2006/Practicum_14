n = int(input())

antonyms = {}
for _ in range(n):
    w1, w2 = input().split()
    w1_low = w1.lower()
    w2_low = w2.lower()
    antonyms[w1_low] = w2_low
    antonyms[w2_low] = w1_low

word = input().lower()
print(antonyms.get(word, word))