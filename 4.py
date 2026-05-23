n = int(input())

forms = {}
for _ in range(n):
    parts = input().split()
    form = parts[0]
    for item in parts[1:]:
        forms[item] = form

item = input()
print(forms.get(item, "Не найдено"))