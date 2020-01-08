"""Implement bit set in Python

url: https://www.acmicpc.net/problem/11723
"""
import sys

input = sys.stdin.readline


class BitSet:
    def __init__(self, size):
        self._set = 0
        self._size = size

    def add(self, v):
        self._set |= (1 << v)

    def has(self, n):
        return 1 if self._set & (1 << n) else 0

    def remove(self, n):
        self._set &= ~(1 << n)

    def toggle(self, n):
        self._set ^= (1 << n)

    def turn_on_all(self):
        self._set = (1 << (self._size+1)) - 1

    def turn_off_all(self):
        self._set >>= (self._size + 1)


if __name__ == '__main__':
    N = int(input())
    bit_set = BitSet(20)

    for _ in range(N):
        cmd, *v = input().strip().split()
        if v:
            v = int(v[0])

        if cmd == 'add':
            bit_set.add(v)
        elif cmd == 'check':
            print(bit_set.has(v))
        elif cmd == 'remove':
            bit_set.remove(v)
        elif cmd == 'toggle':
            bit_set.toggle(v)
        elif cmd == 'all':
            bit_set.turn_on_all()
        elif cmd == 'empty':
            bit_set.turn_off_all()
