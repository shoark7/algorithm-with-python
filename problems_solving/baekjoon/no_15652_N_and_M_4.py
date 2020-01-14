"""Print out permutations with duplications in ascending order

https://www.acmicpc.net/problem/15652
"""
import sys

write = sys.stdout.write


def permutations(n, r):
    chosen = []

    def generate():
        if len(chosen) == r:
            for i in range(len(chosen)):
                write(str(chosen[i]) + ' ')
            write('\n')
            return

        start = chosen[-1] if chosen else 1

        for i in range(start, n + 1):
            chosen.append(i)
            generate()
            chosen.pop()
    generate()


if __name__ == '__main__':
    N, R = (int(n) for n in input().split())
    permutations(N, R)
