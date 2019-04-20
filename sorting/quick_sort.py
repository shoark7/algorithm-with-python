"""Quick sort in Python

Python cache code is brilliant I guess.

Date: 2019/04/20
"""
def quick_sort(arr):
    def sort(lo, hi):
        if lo < hi:
            pivot = partition(lo, hi)
            sort(lo, pivot)
            sort(pivot+1, hi)

    def partition(lo, hi):
        mid = (lo + hi) // 2
        pivot = arr[mid]
        left = lo
        right = hi

        while True:
            while left <= hi and arr[left] < pivot:
                left += 1

            while right >= 0 and pivot < arr[right]:
                right -= 1

            if left >= right:
                return right

            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            left += 1

    sort(0, len(arr)-1)
    return arr


def quick_sort_cache(arr, reverse=True):
    """Quick sort using cache in Python

    This source is from wikipedia.
    It uses cache for quick sort.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less, equal, more = [], [], []

    for n in arr:
        if n < pivot:
            less.append(n)
        elif n == pivot:
            equal.append(n)
        else:
            more.append(n)

    return quick_sort_cache(less, reverse) + equal + quick_sort_cache(more, reverse)
