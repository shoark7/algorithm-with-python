"""Sort algorithm module with Python


This contains all sort algorithm in this directory.
All supports reverse sort and changes target itself(command functions).

Sorts ways are like below:
    1. Bubble sort
    2. Insertion sort
    3. Merge sort
    4. Quick sort + Quick sort with cache
    5. Radix sort(supports only POSITIVE INTEGERS until 18/02/23))
    6. Selection sort
    7. Shell sort

Date: 2018/02/23
"""


def bubble_sort(target, reverse=False):
    """Bubble sort in Python"""
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


def radix_sort(target, reverse=False):
    """Radix sort in Python

    This sort uses 'queue way'. But simply uses list in Python.
    Also it assumes all elements in target are POSITIVE INTEGERS.
    """
    def get_nth_digit(n, d):
        n %= 10 ** d
        return n // 10 ** (d-1)

    digit = 0
    max_value = max(target)
    while max_value:
        digit += 1
        max_value //= 10

    sort_queue = list()
    iter_range = range(10) if not reverse else range(9, -1, -1)

    for d in range(1, digit+1):
        for i in iter_range:
            for n in target:
                if get_nth_digit(n, d) == i:
                    sort_queue.append(n)
        target[:] = sort_queue.copy()  # Can you guess why assignment is like this?
        sort_queue.clear()
    return target


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


def shell_sort(arr, reverse=False):
    """Shell sort in Python"""
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
