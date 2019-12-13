"""Get last number in the deck

url: https://www.acmicpc.net/problem/2164
"""
from collections import deque
from math import log2


# Brute force
def last_man_standing(N):
    deck = deque(range(1, N+1))
    is_throw_turn = True

    while len(deck) > 1:
        first = deck.popleft()
        if not is_throw_turn:
            deck.append(first)

        is_throw_turn ^= True

    return deck[0]


# O(1) Way
def last_man_standing(N):
    e = int(log2(N))
    n = 2 ** e
    return N if (N & (N - 1)) == 0 else (N - n) * 2


if __name__ == '__main__':
    n = int(input())
    print(last_man_standing(n))
