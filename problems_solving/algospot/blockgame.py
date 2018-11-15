"""Decide if player this turn can win the game with given board

:input:
3
.....
.##..
##..#
#.###
..#..
.....
.....
.....
.....
.....
#..##
##.##
##.##
#...#
##.##

:return:
WINNING
LOSING
WINNING

url: https://algospot.com/judge/problem/read/BLOCKGAME
ID : BLOCKGAME
"""

"""My fucking code: I guessed wrong...
SIZE = 5
BLOCKS = [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)],
          [(0, 1), (1, 1)], [(1, 0), (1, -1)], [(0, -1), (-1, -1)], [(-1, 0), (-1, 1)]]


def can_win(board):
    cache = [-1 for _ in range(1 << 25)]

    def unplace(board, r, c, block):
        board[r][c] = '.'
        for new_r, new_c in block:
            if (0 <= r+new_r <= SIZE-1) and (0 <= c+new_c <= SIZE-1):
                board[r+new_r][c+new_c] = '.'

    def place(board, r, c, block):
        ok = True
        board[r][c] = '#'
        for new_r, new_c in block:
            if (0 <= r+new_r <= SIZE-1) and (0 <= c+new_c <= SIZE-1) and board[r+new_r][c+new_c] == '.':
                board[r+new_r][c+new_c] = '#'
            else:
                unplace(board, r, c, block)
                ok = False
                break
        return ok

    def board_to_int(board):
        int_board = 0
        for r in range(SIZE):
            for c in range(SIZE):
                int_board *= 2
                if board[r][c] == '#':
                    int_board += 1
        return int_board

    def is_finished(board):
        for r in range(SIZE):
            for c in range(SIZE-1):
                if board[r][c] == '.' and board[r][c+1] == '.':
                    return False

        for c in range(SIZE):
            for r in range(SIZE-1):
                if board[r][c] == '.' and board[r+1][c] == '.':
                    return False

        return True

    def play(board):
        if is_finished(board):
            return False
        int_board = board_to_int(board)
        if cache[int_board] != -1:
            return cache[int_board]

        result = 1
        for r in range(SIZE):
            for c in range(SIZE):
                if board[r][c] == '.':
                    for block in BLOCKS:
                        is_block_put = place(board, r, c, block)
                        if is_block_put:
                            tmp = play(board)
                            result = min(result, tmp)
                            unplace(board, r, c, block)
        cache[int_board] = result

        return 1 if not result else 0


    return 'WINNING' if play(board) else 'LOSING'
"""
SIZE = 5


def get_cell_num(r, c):
    return 1 << (r * 5 + c)

def make_move():
    ret = []
    for r in range(SIZE-1):
        for c in range(SIZE-1):
            cells = []
            for dr in range(2):
                for dc in range(2):
                    new_cell = get_cell_num(r+dr, c+dc)
                    cells.append(new_cell)

            for i in range(4):
                ret.append(sum(cells) - cells[i])

    for i in range(SIZE):
        for j in range(SIZE-1):
            ret.append(get_cell_num(i, j) + get_cell_num(i, j+1))
            ret.append(get_cell_num(j, i) + get_cell_num(j+1, i))

    return ret

ALL_MOVES = make_move()
print(ALL_MOVES)
cache = [-1 for _ in range(1<<25)]

def can_win(board):
    i = 0
    def board_to_int(board):
        int_board = 0
        for r in range(SIZE):
            for c in range(SIZE):
                int_board *= 2
                if board[r][c] == '#':
                    int_board += 1
        return int_board


    def play(board):
        nonlocal i
        global cache
        print(i)
        i += 1
        if cache[board] != -1:
            return cache[board]
        ret = 0
        for m in ALL_MOVES:
            if (m & board) == 0:
                if play(board | m) == 0:
                    ret = 1
                    break
        cache[board] = ret
        return ret

    int_board = board_to_int(board)
    ret = play(int_board)
    return 'WINNING' if ret else 'LOSING'


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        board = []
        for _ in range(SIZE):
            board.append([c for c in input()])
        ans.append(can_win(board))

    for n in ans:
        print(n)
