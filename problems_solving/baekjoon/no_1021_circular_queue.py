"""Get least number of calculations to rotate arrays as given

url: https://www.acmicpc.net/problem/1021
"""
def min_calcs(arr, targets):
    """We assume there are no duplicate values in array"""
    size = len(arr)
    ans = 0

    for t in targets:
        k = arr.index(t)
        ans += min(k+1, size-k-1)
        arr = arr[k+1:] + arr[:k+1]
        arr.pop()
        size -= 1

    return ans


if __name__ == '__main__':
    N, _ = (int(n) for n in input().split())
    targets = [int(n) for n in input().split()]
    arr = list(range(1, N+1))
    arr = arr[::-1]
    print(min_calcs(arr, targets))
