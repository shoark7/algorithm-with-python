"""Print out permutations with duplications

https://www.acmicpc.net/problem/15651
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

        for i in range(1, n + 1):
            chosen.append(i)
            generate()
            chosen.pop()
    generate()


if __name__ == '__main__':
    N, R = (int(n) for n in input().split())
    permutations(N, R)
