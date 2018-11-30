"""Get minimum number of chaning color of light bulbs until all colors are same

:input:
10 3
1 1 2 3 3 3 2 2 1 1

:return:
2

url: https://www.acmicpc.net/problem/2449
"""
def min_count(arr):
    N = len(arr)
    cache = [[-1 for _ in range(N)] for _ in range(N)]

    def get(lo, hi):
        if lo == hi:
            return 0
        elif cache[lo][hi] != -1:
            return cache[lo][hi]

        if hi > 0 and arr[hi] == arr[hi-1]:
            ret = get(lo, hi-1)
        elif lo + 1 < N and arr[lo] == arr[lo+1]:
            ret = get(lo+1, hi)
        else:
            ret = 9999
            for k in range(lo, hi):
                ret = min(ret, get(lo, k) + get(k+1, hi) + (arr[lo] != arr[k+1]))

        cache[lo][hi] = ret
        return ret

    return get(0, N-1)


if __name__ == '__main__':
    N, K = (int(n) for n in input().split())
    arr = [int(n) for n in input().split()]
    print(arr)

    print(min_count(arr))
