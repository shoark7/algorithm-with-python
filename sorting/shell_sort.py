"""Shell sort in Python

Date: 2018/02/20
"""


def shell_sort(arr, reverse=False):
    gap = len(arr) // 3 + 1
    n = len(arr) // gap

    def sort_by_gap(gap, n):
        if not reverse:
            for s in range(gap):
                for k in range(1, n):
                    while k > 0:
                        if arr[s+gap*k] < arr[s+gap*(k-1)]:
                            arr[s+gap*k], arr[s+gap*(k-1)] = arr[s+gap*(k-1)], arr[s+gap*k]
                            k -= 1
                        else:
                            break
        else:
            for s in range(gap):
                for k in range(1, n):
                    while k > 0:
                        if arr[s+gap*k] > arr[s+gap*(k-1)]:
                            arr[s+gap*k], arr[s+gap*(k-1)] = arr[s+gap*(k-1)], arr[s+gap*k]
                            k -= 1
                        else:
                            break

        new_gap = gap // 2
        if new_gap <= 0:
            return

        sort_by_gap(new_gap, len(arr) // new_gap)

    sort_by_gap(gap, n)

    return arr
