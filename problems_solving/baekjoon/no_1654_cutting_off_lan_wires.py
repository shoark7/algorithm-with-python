"""Get maximum length of cutted lan wires

url: https://www.acmicpc.net/problem/1654
"""
import sys

input = sys.stdin.readline


def max_wire_length(arr, MIN_REQUIRED):
    def number_of_wires(length):
        return sum(n // length for n in arr)

    def search_max_len(lo, hi):
        if lo == hi:
            return hi

        mid = (lo + hi) // 2 + 1  # 이 코드가 핵심. 왜 1을 더할까요?
        if number_of_wires(mid) >= MIN_REQUIRED:
            return search_max_len(mid, hi)
        else:
            return search_max_len(lo, mid-1)

    return search_max_len(1, max(arr))


if __name__ == '__main__':
    K, MIN_REQUIRED = [int(n) for n in input().split()]
    arr = []

    for _ in range(K):
        arr.append(int(input()))

    print(max_wire_length(arr, MIN_REQUIRED))
