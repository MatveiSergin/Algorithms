def dijkstra(matrix, start, end):
    ways = [float("inf")] * len(matrix)

    point = start
    visited = set()
    visited.add(point)

    ways[point] = 0

    while point != -1:
        for i in range(len(matrix[point])):
            if i not in visited and matrix[point][i] > 0:
                cur_way = matrix[point][i] + ways[point]
                if cur_way < ways[i]:
                    ways[i] = cur_way

        mn_ind = -1
        m = float("inf")
        for i, j in enumerate(ways):
            if j < m and i not in visited:
                mn_ind = i
                m = j
        point = mn_ind
        if point != -1:
            visited.add(point)
    return ways[end]

def main():
    matrix = (
        (0, 4, 3, 0),
        (4, 0, 2, 0),
        (3, 2, 0, 6),
        (0, 0, 6, 0)
    )
    start = 0
    end = 3
    print(dijkstra(matrix, start, end))

if __name__ == '__main__':
    main()