"""Selection sort

Date : 2018/02/05
"""


def selection_sort(target, reverse=False):
    """Selecetion sort in Python"""
    for i in range(len(target)):
        tmp = i
        if not reversed:
            for j in range(i, len(target)):
                if target[tmp] > target[j]:
                    tmp = j
        else:
            for j in range(i, len(target)):
                if target[tmp] < target[j]:
                    tmp = j
        target[tmp], target[i] = target[i], target[tmp]
    return target
