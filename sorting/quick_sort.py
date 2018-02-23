"""Quick sort in Python

This code is mainly from wikipedia.
Python cache code is brilliant I guess.

Date: 2018/02/23
"""


def quick_sort(arr, reverse=False):
    """Quick sort in Python

    This uses first element of sublist as a pivot.
    """
    def partition(start, end):
        if end - start < 1:
            return
        pivot = start
        left = start + 1
        right = end
        done = False
        if not reverse:
            while not done:
                while left <= right and arr[left] <= arr[pivot]:
                    left += 1
                while left <= right and arr[right] >= arr[pivot]:
                    right -= 1
                if right < left:
                    done = True
                else:
                    arr[left], arr[right] = arr[right], arr[left]
        else:
            while not done:
                while left <= right and arr[left] >= arr[pivot]:
                    left += 1
                while left <= right and arr[right] <= arr[pivot]:
                    right -= 1
                if right < left:
                    done = True
                else:
                    arr[left], arr[right] = arr[right], arr[left]

        arr[right], arr[start] = arr[start], arr[right]
        partition(start, right - 1)
        partition(right + 1, end)

    partition(0, len(arr)-1)

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
