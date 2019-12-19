"""Get number of each card in deck

url: https://www.acmicpc.net/problem/10816
"""
from collections import Counter


# 1. Using Binary search: O(NlogN + MlogN)
def number_of_cards(arr, target, is_sorted=True):
    N = len(arr)

    def get_lower_idx(lo, hi):
        if lo == hi:
            return lo

        mid = (lo + hi) // 2
        if arr[mid] >= target:
            return get_lower_idx(lo, mid)
        else:
            return get_lower_idx(mid+1, hi)

    def get_upper_idx(lo, hi):
        if lo == hi:
            return lo

        mid = (lo + hi) // 2 + 1
        if arr[mid] <= target:
            return get_upper_idx(mid, hi)
        else:
            return get_upper_idx(lo, mid-1)


    i, j = get_lower_idx(0, N-1), get_upper_idx(0, N-1)

    if arr[i] != target:
        return 0
    else:
        return j - i + 1


# 2. Using Hash: O(N + M)
def number_of_cards(arr, targets):
    counter = Counter(arr)
    ans = []

    for t in targets:
        ans.append(counter[t])
    return ans


if __name__ == '__main__':
    input()
    arr = [int(n) for n in input().split()]
    # arr.sort()
    input()
    targets = [int(n) for n in input().split()]

    # 여기서는 해쉬 자료구조로 통과하자. 파이썬으로는 이진탐색으로 안 된다...
    print(' '.join(str(n) for n in number_of_cards(arr, targets)))
