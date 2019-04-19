"""Merge sort in Python


Updated to version 2:
    This time, divide returns [lo, hi] which directs to start and end points of an interval.

Date: 2019/04/19
"""
def merge_sort(arr):
    def divide(lo, hi):
        if lo == hi:
            return (lo, lo)

        mid = (lo + hi) // 2
        left = divide(lo, mid)
        right = divide(mid+1, hi)

        merge(left, right)
        return (lo, hi)


    def merge(left, right):
        ll, lh = left
        rl, rh = right

        left = ll
        right = rl
        tmp = []

        while left <= lh or right <= rh:
            if left > lh or (right <= rh and arr[right] < arr[left]):
                tmp.append(arr[right])
                right += 1
            else:
                tmp.append(arr[left])
                left += 1

        arr[ll:rh+1] = tmp

    return arr if not arr else (divide(0, len(arr)-1) and arr)
