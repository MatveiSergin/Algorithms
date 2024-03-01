N = int(input())
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
queue = []
field = [[-1] * N for i in range(N)]
field[x1][y1] = 0
queue.append((x1, y1))
horse_moves = [(i, j) for i in (-1, 1, -2, 2) for j in (-1, 1, -2, 2) if abs(i) != abs(j)]

while queue:
    x_old, y_old = queue.pop(0)
    for move in horse_moves:
        x_new, y_new = x_old + move[0], y_old + move[1]
        if 0 <= x_new <= N-1 and 0 <= y_new <= N-1:
            if field[x_new][y_new] < 0:
                field[x_new][y_new] = field[x_old][y_old] + 1
                queue.append((x_new, y_new))

print(field[x2][y2])


