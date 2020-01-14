"""Implement queue and do some jobs

https://www.acmicpc.net/problem/18258
"""
from collections import deque
import sys

input = sys.stdin.readline
write = sys.stdout.write


if __name__ == '__main__':
    queue = deque()
    N = int(input())

    for _ in range(N):
        cmd, *v = input().strip().split()
        if cmd == 'push':
            v = v[0]
            queue.append(v)
        elif cmd == 'front':
            if not queue:
                write('-1\n')
            else:
                write(queue[0] + '\n')
        elif cmd == 'back':
            if not queue:
                write('-1\n')
            else:
                write(queue[-1] + '\n')
        elif cmd == 'size':
            write(str(len(queue)) + '\n')
        elif cmd == 'empty':
            if not queue:
                write('1\n')
            else:
                write('0\n')
        elif cmd == 'pop':
            if not queue:
                write('-1\n')
            else:
                write(queue.popleft() + '\n')
