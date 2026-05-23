def find_shortest_distance(cities, start, """
    Находит кратчайшее расстояние между двумя городами.

    Параметры:
        cities (dict): Словарь, где ключ - название города,
                       значение - список кортежей (сосед, расстояние).
        start (str): Начальный город.
        finish (str): Конечный город.

    Возвращает:
        int: Кратчайшее расстояние между start и finish.
             Если пути не существует, возвращает -1.
    """
    # Расстояния до всех городов
    distances = {}
    for city in cities:
        distances[city] = float('inf')
    distances[start] = 0
    
    unvisited = list(cities.keys())
    
    while unvisited:
        # Находим город с минимальным расстоянием среди непосещённых
        current = None
        for city in unvisited:
            if current is None or distances[city] < distances[current]:
                current = city
        
        if current == finish:  
            return distances[current]
        
        if distances[current] == float('inf'):  
            break
        
        # Обновляем расстояния до соседей
        for neighbor, dist in cities[current]:
            if distances[neighbor] > distances[current] + dist:
                distances[neighbor] = distances[current] + dist
        
        unvisited.remove(current)
    
    return distances[finish] if distances[finish] != float('inf') else -1

n = int(input("Введите количество городов: "))
m = int(input("Введите количество дорог: "))

cities = {}

for i in range(m):
    line = input()
    parts = line.split()
    city1 = parts[0]
    city2 = parts[1]
    distance = int(parts[2])
    
    # Добавляем дорогу в обе стороны
    if city1 not in cities:
        cities[city1] = []
    if city2 not in cities:
        cities[city2] = []
    
    cities[city1].append((city2, distance))
    cities[city2].append((city1, distance))

# Последняя строка - города, между которыми ищем путь
last_line = input()
parts = last_line.split()
start_city = parts[0]
finish_city = parts[1]

result = find_shortest_distance(cities, start_city, finish_city)
print(result)
