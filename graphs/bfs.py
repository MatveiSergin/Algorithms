visited = set()
queue = []
graph = [
    [1, 2],
    [0, 3, 4],
    [0],
    [1],
    [2, 3]
]
def bfs(start):
    visited.add(start)
    for child in graph[start]:
        if child not in visited:
            queue.append(child)
    del queue[0]
    if len(queue):
        bfs(queue[0])
start = int(input())
queue.append(start)
bfs(start)