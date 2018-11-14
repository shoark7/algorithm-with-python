"""Decide who would win in tictactoe game when they play their best

:input:
3
...
...
...
xx.
oo.
...
xox
oo.
x.x

:return:

TIE
x
o
"""
def someone_won(board, turn):
    if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
        return True
    elif board[2][0] == turn and board[1][1] == turn and board[0][2] == turn:
        return True
    elif board[0][0] == turn and board[0][1] == turn and board[0][2] == turn:
        return True
    elif board[1][0] == turn and board[1][1] == turn and board[1][2] == turn:
        return True
    elif board[2][0] == turn and board[2][1] == turn and board[2][2] == turn:
        return True
    elif board[0][0] == turn and board[1][0] == turn and board[2][0] == turn:
        return True
    elif board[0][1] == turn and board[1][1] == turn and board[2][1] == turn:
        return True
    elif board[0][2] == turn and board[1][2] == turn and board[2][2] == turn:
        return True
    else:
        return False


def board_to_int(board):
    ret = 0
    for r in range(3):
        for c in range(3):
            ret *= 3
            if board[r][c] == 'o':
                ret += 1
            elif board[r][c] == 'x':
                ret += 2
    return ret


def lets_play(board):
    cache = [-2 for _ in range(3 ** 9)]

    def can_win(board, turn):
        opponent = 'o' if turn == 'x' else 'x'
        if someone_won(board, opponent):
            return -1

        int_board = board_to_int(board)
        if cache[int_board] != -2:
            return cache[int_board]

        tmp = 2
        for r in range(3):
            for c in range(3):
                if board[r][c] == '.':
                    board[r][c] = turn
                    tmp = min(tmp, can_win(board, opponent))
                    board[r][c] = '.'

        if tmp == 2 or tmp == 0:
            cache[int_board] = 0
            return 0
        else:
            cache[int_board] = -tmp
            return -tmp

    xs = os = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'o':
                os += 1
            elif board[r][c] == 'x':
                xs += 1

    if xs == os:
        turn = 'x'
    else:
        turn = 'o'

    result = can_win(board, turn)

    if result == 0:
        return 'TIE'
    elif result == 1:
        return turn
    else:
        return 'o' if turn == 'x' else 'x'


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        board = []
        for _ in range(3):
            board.append([x for x in input()])
        ans.append(lets_play(board))

    for n in ans:
        print(n)
