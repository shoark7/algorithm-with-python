"""Return whether element is in the array

url: https://www.acmicpc.net/problem/1920
"""
def binary_search(arr, v, is_sorted=True):
    SIZE = len(arr)

    if not is_sorted:
        arr.sort()

    def move_on(lo, hi):
        if lo == hi:
            return (True, lo) if arr[lo] == v else (False, -1)

        mid = (lo + hi) // 2
        if arr[mid] >= v:
            return move_on(lo, mid)
        else:
            return move_on(mid+1, hi)

    return move_on(0, SIZE-1)


if __name__ == '__main__':
    input()
    arr = [int(n) for n in input().split()]
    arr.sort()
    input()
    targets = [int(n) for n in input().split()]

    for t in targets:
        exists, _ = binary_search(arr, t)
        print(1 if exists else 0)
