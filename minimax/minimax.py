def check_win(board, step):
    return (board[0] == step and board[1] == step and board[2] == step) or (
            board[3] == step and board[4] == step and board[5] == step) or (
            board[6] == step and board[7] == step and board[8] == step) or (
            board[0] == step and board[3] == step and board[6] == step) or (
            board[1] == step and board[4] == step and board[7] == step) or (
            board[2] == step and board[5] == step and board[8] == step) or (
            board[0] == step and board[4] == step and board[8] == step) or (
            board[2] == step and board[4] == step and board[6] == step)

def is_valid_move(move, board):
    return board[move] not in 'X0' and type(move) == int and move in range(9)

def emptyIndexies(board):
    return [i for i in range(9) if board[i] != 'X' and board[i] != '0']

def minimax(newboard, player):
    free_positions = emptyIndexies(newboard)
    if check_win(newboard, '0'):
        return {'score': -10}
    elif check_win(newboard, 'X'):
        return {'score': 10}
    elif len(free_positions) == 0:
        return {'score': 0}

    moves = []

    for i in range(len(free_positions)):
        move = {}
        move['index'] = free_positions[i]
        newboard[free_positions[i]] = player

        if player == 'X':
            result = minimax(newboard, '0')
            move["score"] = result["score"]
        else:
            result = minimax(newboard, 'X')
            move["score"] = result["score"]

        newboard[free_positions[i]] = move['index']

        moves.append(move)

    if (player == 'X'):
        total = -10000
        for i in range(len(moves)):
            if moves[i]['score'] > total:
                total = moves[i]['score']
                bestMove = i
    else:
        total = 10000
        for i in range(len(moves)):
            if (moves[i]['score'] < total):
                total = moves[i]['score']
                bestMove = i
    return moves[bestMove]

def draw_board(board):
    for i in range(9):
        if (i == 3 or i == 6) and i != 0:
            print('\n')
            print(board[i], end=' ')
        else:
            print(board[i], end=' ')
    print('\n')

def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    best_move = {'score': 0, 'index': -10}
    counter = 0
    while any(j in board for j in range(9)) and not (best_move['score']==10 or best_move['score']==-10):
        step = int(input('Введите ваш ход: '))
        board[step] = '0'
        counter += 1
        if counter == 5:
            draw_board(board)
            break
        best_move = minimax(board, 'X')
        board[best_move['index']] = 'X'
        draw_board(board)

    if best_move['score'] == 10:
        print("Вы проиграли")
    elif best_move['score'] == 0:
        print("Ничья")
    else:
        print("Вы победили")

if __name__ == '__main__':
    main()