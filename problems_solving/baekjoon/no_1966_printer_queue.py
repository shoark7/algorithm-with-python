"""Print order of specific number to be printed

url: https://www.acmicpc.net/problem/1966
"""
from collections import deque


def get_order(arr, nth):
    arr = deque((i == nth, n) for i, n in enumerate(arr))
    importances = [0] * 10

    for i, n in arr:
        importances[n] += 1

    count = 1
    while arr:
        is_target, n = arr.popleft()

        if any(importances[big] > 0 for big in range(n+1, 10)):
            arr.append((is_target, n))
        else:
            if is_target:
                return count
            else:
                importances[n] -= 1
                count += 1


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        _, nth = (int(n) for n in input().split())
        arr = [int(n) for n in input().split()]
        ans.append(get_order(arr, nth))

    for n in ans:
        print(n)
