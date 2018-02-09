"""Merge sort in Python

Date: 2018/02/09
"""


def merge_sort(target, reverse=False):
    """Merge sort in Python"""
    def divide(start, end):
        if end - start > 1:
            mid = (end + start) // 2
            divide(start, mid)
            divide(mid+1, end)
        merge(start, end)

    def merge(start, end):
        mid = (start + end) // 2 + 1
        left, right = start, mid
        tmp_list = []
        if not reverse:
            while left < mid and right <= end:
                if target[left] >= target[right]:
                    tmp_list.append(target[right])
                    right += 1
                else:
                    tmp_list.append(target[left])
                    left += 1
        else:
            while left < mid and right <= end:
                if target[left] <= target[right]:
                    tmp_list.append(target[right])
                    right += 1
                else:
                    tmp_list.append(target[left])
                    left += 1

        while left < mid:
            tmp_list.append(target[left])
            left += 1

        while right <= end:
            tmp_list.append(target[right])
            right += 1

        target[start:end+1] = tmp_list

    divide(0, len(target)-1)
    return target
