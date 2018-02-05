"""Binary search module

    Start Date: 2017/12/08
    Last modified Date: 2017/12/08

    github.com/shoark7
"""
__version__ = '1.1.0'


def binary_search(value, target, reverse=False, changed=False):
    """Binary search in Python

    This code is designed to be scalable, considering this kind of things,
        1. ascending or descending can be chosen.
        2. target list to be ransacked can be sorted during the search.
        3. And more...

    :input:
        value:   Value to be searched
        target:  List or something to be ransacked.
        reverse: Whether search to be done in descending or not.
        changed: Whether target to be changed during searching or not.

    :return:
        Index of the value in target.
        If value is not in target, returns -1.
    """
    if value not in target:
        return -1

    if changed:
        target.sort(reverse=reverse)
        ordered = target
    else:
        ordered = sorted(target, reverse=reverse)

    def search(start, end):
        mid = (start + end) // 2
        if value > ordered[mid]:
            return search(mid, end)
        elif value < ordered[mid]:
            return search(start, mid)
        else:
            return mid

    return search(0, len(ordered)-1)
