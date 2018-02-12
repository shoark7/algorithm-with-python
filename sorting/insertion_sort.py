"""Insertion sort in Python


Date: 2018/02/10
"""


def insertion_sort(target, reverse=False):
    """Insertion sort in Python"""
    if reverse:
        for i in range(len(target)):
            tmp = target[i]
            for j in range(i-1, -1, -1):
                if tmp > target[j]:
                    target[j+1] = target[j]
                    target[j] = tmp
                else:
                    break
    else:
        for i in range(len(target)):
            tmp = target[i]
            for j in range(i-1, -1, -1):
                if tmp < target[j]:
                    target[j+1] = target[j]
                    target[j] = tmp
                else:
                    break

    return target
