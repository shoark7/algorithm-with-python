"""Bubble sort in Python

Date: 2018/02/08
"""


def bubble_sort(target, reverse=False):
    length = len(target)
    if reverse:
        for i in range(length-1):
            for j in range(length-1):
                if target[j] < target[j+1]:
                    target[j], target[j+1] = target[j+1], target[j]
    else:
        for i in range(length-1):
                for j in range(length-1):
                    if target[j] > target[j+1]:
                        target[j], target[j+1] = target[j+1], target[j]
    return target
