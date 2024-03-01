def dfs(graph, start, visited=set()):
    visited.add(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next)
    return visited

graph = {0: [1, 2],
         1: [0, 3, 4],
         2: [0],
         3: [1],
         4: [2, 3]}

print(1 in dfs(graph, 0))