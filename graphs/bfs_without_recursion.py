def bfs_without_recursion(graph, start):
    queue = []
    visited = set()
    visited.add(start)
    for child in graph[start]:
        queue.append(child)

    while(len(queue) != 0):
        start = queue[0]
        del queue[0]
        for child in graph[start]:
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return visited

graph = {0: [1, 2],
         1: [0, 3, 4],
         2: [0],
         3: [1],
         4: [2, 3]}

visited = bfs_without_recursion(graph, 0)
print(4 in visited)