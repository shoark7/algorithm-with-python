"""Solve Boggle problem in algospot

:input:
1
URLPM
XPRET
GIAET
XTNZY
XOQRS
6
PRETTY
GIRL
REPEAT
KARA
PANDORA
GIAZAPX

:return:
PRETTY YES
GIRL YES
REPEAT YES
KARA NO
PANDORA NO
GIAZAPX YES


url: https://algospot.com/judge/problem/read/BOGGLE
ID : BOGGLE
"""
SIZE = 5
MOVES = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

def board_to_int(board):
    ret = 0
    size = len(board)
    for x in range(size):
        for y in range(size):
            ret *= size
            ret += board[x][y]
    return ret


def has_word(board, word):
    global cache, MOVES, SIZE




if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        board = []
        for _ in range(SIZE):
            board.append(input())
        cache = [[[-1 for _ in range(26)] for _ in range(SIZE)] for _ in range(SIZE)]
        N = int(input())
        for _ in range(N):
            word = input()
            # ans.append(word + (' YES' if has_word(board, word) else ' NO'))
            ans.append(word + (' YES' if has_word(board) else ' NO'))

    for n in ans:
        print(n)
