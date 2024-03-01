INF = 10 ** 9
dist = [INF] * N
dist[0] = 0
used = [False] * N
ans = 0
for i in range(N):
    min_dist = INF
    for j in range(N):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            u = j
    ans += min_dist
    used[u] = True
    for v in range(N):
        dist[v] = min(dist[v], W[u][v])