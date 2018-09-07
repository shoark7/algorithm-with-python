"""Solve Boggle problem in algospot

It has some meaningful solving ways and I'll make it one by one in a same file


https://algospot.com/judge/problem/read/BOGGLE
"""
from collections import namedtuple

Point = namedtuple('Point', ['y', 'x'])
COORDS = [Point(-1, -1), Point(-1, 0), Point(-1, 1),
          Point(0, -1), Point(0, 0), Point(0, 1),
          Point(1, -1), Point(1, 0), Point(1, 1),]
SIZE = 5

def is_in_range(y, x):
    return True if 0 <= x <= SIZE and 0 <= y <= SIZE else False


def has_word(y, x, word):
    if not is_in_range(y, x):
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True

    for direction in range(len(COORDS)):
        newy, newx = y + directiony, x + direction.x
        if hasword(newy, newyx, word[1:]):
            return True
    return False


if __name__ == '__main__':
    board = [list('URLPM'), list('XPRET'), list('GIAET'),
             list('XTNZY'), list('XOQRS')]
    tests = ['PRETTY', 'GIRL', 'REPEAT', 'KARA', 'PANDORA', 'GIAZAPX']

    for word in tests:
        print(word, 'YES' if has_word(word) else 'NO')
