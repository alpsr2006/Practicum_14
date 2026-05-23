def count_descendants(person, children):
    """
    Рекурсивно подсчитывает количество потомков для заданного человека.

    Параметры:
        person (str): Имя человека, для которого считаем потомков.
        children (dict): Словарь, где ключ - родитель,
        значение - список детей.

    Возвращает:
        int: Общее количество потомков (дети, внуки, правнуки и т.д.).
    """
    total = 0
    for child in children.get(person, []):
        total += 1 + count_descendants(child, children)
    return total


n = int(input())

children = {}
for _ in range(n):
    parent, child = input().split()
    children.setdefault(parent, []).append(child)

name = input()
print(count_descendants(name, children))