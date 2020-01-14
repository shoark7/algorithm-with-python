"""Print out permutations

https://www.acmicpc.net/problem/15649
"""
import sys

write = sys.stdout.write


def permutations(n, r):
    chosen = []
    used = [0] * (n + 1)

    def generate():
        if len(chosen) == r:
            for i in range(len(chosen)):
                write(str(chosen[i]) + ' ')
            write('\n')
            return

        for i in range(1, n + 1):
            if not used[i]:
                chosen.append(i)
                used[i] = 1
                generate()
                chosen.pop()
                used[i] = 0
    generate()


if __name__ == '__main__':
    N, R = (int(n) for n in input().split())
    permutations(N, R)
