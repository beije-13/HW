
source_map = {
    'Почтовое отделение': (0, 2),
    'Ул. Грибоедова, 104/25 ': (2, 5),
    'Ул. Бейкер стрит, 221б': (5, 2),
    'Ул. Большая Садовая, 302-бис': (6, 6),
    'Вечнозелёная Аллея, 742': (8, 3)
}


def find_shortest_path(given_map):
    point1 = given_map.pop('Почтовое отделение')
    s_p = [point1, '->']
    start = point1

    for i in range(len(given_map)):
        shortest_path = []
        for key, point2 in given_map.items():
            res = calculate_distance(point1=start, point2=point2)
            if not shortest_path:
                shortest_path = [key, point2, [res]]
            elif res < shortest_path[2][0]:
                shortest_path = [key, point2, [res]]
        if i >= 1:
            path_sum = s_p[-2][0] + shortest_path[2][0]
            s_p.append(shortest_path[1])
            s_p.append([path_sum])
            s_p.append('->')
        else:
            s_p.append(shortest_path[1])
            s_p.append(shortest_path[2])
            s_p.append('->')

        start = shortest_path[1]
        if len(given_map) != 1:
            given_map.pop(shortest_path[0])
        else:
            comeback = calculate_distance(point1=shortest_path[1], point2=point1)
            path_sum = s_p[-2][0] + comeback
            s_p.append(point1)
            s_p.append([path_sum])
            s_p.append('=')
            s_p.append([path_sum])
    return s_p


def calculate_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


print(' '.join(map(str, find_shortest_path(source_map))))
