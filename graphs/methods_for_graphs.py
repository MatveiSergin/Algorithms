visited_for_bfs = set()
queue_for_bfs = []
def bfs(graph, start):
    visited_for_bfs.add(start)
    for child in graph[start]:
        if child not in visited_for_bfs:
            queue_for_bfs.append(child)
    del queue_for_bfs[0]
    if queue_for_bfs:
        bfs(graph, queue_for_bfs[0])

def bfs_without_recursion(graph, start):
    queue2 = []
    visited = set()
    visited.add(start)
    for child in graph[start]:
        queue2.append(child)

    while(len(queue2) != 0):
        start = queue2[0]
        del queue2[0]
        for child in graph[start]:
            if child not in visited:
                queue2.append(child)
                visited.add(child)

    return visited

def dfs(graph, start, visited=set()):
    visited.add(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next)
    return visited

def main():
    graph = {0: [1, 2],
             1: [0, 3, 4],
             2: [0],
             3: [1],
             4: [2, 3]}
    queue_for_bfs.append(0)
    bfs(graph, 0)
    print(4 in visited_for_bfs)
    print(4 in dfs(graph, 0))
    print(4 in bfs_without_recursion(graph, 0))

if __name__ == '__main__':
    main()