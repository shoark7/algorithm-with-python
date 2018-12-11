"""Binary search module

    Start Date: 2017/12/08
    Last modified Date: 2018/12/11

    github.com/shoark7
"""
__version__ = '2.0.0'


def binary_search(arr, v):
    arr.sort()
    def find(lo, hi):
        mid = (lo + hi) // 2
        if lo == hi:
            return lo if arr[lo] == v else -1
        elif arr[mid] < v:
            return find(mid+1, hi)
        else:
            return find(lo, mid)

    return find(0, len(arr)-1)
