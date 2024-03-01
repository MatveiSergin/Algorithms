from heapq import heappush, heappop, merge

end = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
def get_h(board):
    h = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and board[i][j] != end[i][j]:
                h += 1
    return h

def is_goal(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != end[i][j]:
                return False
    return True
def get_neighbour(board, g):
    queue = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                ind_0 = (i, j)
    if ind_0[1] > 0:
        zero_left = [board[0].copy(), board[1].copy(), board[2].copy()]
        number = zero_left[ind_0[0]][ind_0[1] - 1]
        zero_left[ind_0[0]][ind_0[1] - 1] = 0
        zero_left[ind_0[0]][ind_0[1]] = number
        heappush(queue, (g + get_h(zero_left), g, zero_left.copy()))
    if ind_0[1] < len(board[0]) - 1:
        zero_right = [board[0].copy(), board[1].copy(), board[2].copy()]
        number = zero_right[ind_0[0]][ind_0[1] + 1]
        zero_right[ind_0[0]][ind_0[1] + 1] = 0
        zero_right[ind_0[0]][ind_0[1]] = number
        heappush(queue, (g + get_h(zero_right), g,  zero_right.copy()))
    if ind_0[0] > 0:
        zero_up = [board[0].copy(), board[1].copy(), board[2].copy()]
        number = zero_up[ind_0[0] - 1][ind_0[1]]
        zero_up[ind_0[0] - 1][ind_0[1]] = 0
        zero_up[ind_0[0]][ind_0[1]] = number
        heappush(queue, (g + get_h(zero_up), g, zero_up.copy()))
    if ind_0[0] < len(board[0]) - 1:
        zero_down = [board[0].copy(), board[1].copy(), board[2].copy()]
        number = zero_down[ind_0[0] + 1][ind_0[1]]
        zero_down[ind_0[0] + 1][ind_0[1]] = 0
        zero_down[ind_0[0]][ind_0[1]] = number
        heappush(queue, (g + get_h(zero_down), g, zero_down.copy()))
    return queue

def find_ans(start):
    g = 1
    queue = get_neighbour(start, g)
    while True:
        data = heappop(queue)
        old_g = data[1]
        new_board = data[2]
        if is_goal(new_board):
            print("GOAL", g)
            break
        else:
            queue = list(merge(queue, get_neighbour(new_board, old_g + 1)))
        g += 1

def main():
    start = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]
    find_ans(start)

if __name__ == '__main__':
    main()

