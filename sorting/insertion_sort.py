"""Insertion sort in Python


Date: 2018/03/02
"""


def insertion_sort(arr, reverse=False):
    """Insertion sort in Python"""
    length = len(arr)

    if reverse:
        for i in range(1, length):
            while i >= 1:
                if arr[i] > arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    i -= 1
                else:
                    break
    else:
        for i in range(1, length):
            while i >= 1:
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    i -= 1
                else:
                    break
    return arr
