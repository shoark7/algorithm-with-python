"""Sort algorithm module with Python


This contains all sort algorithm in this directory.
All supports reverse sort and changes arr itself(command functions).

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


def bubble_sort(arr, reverse=False):
    """Bubble sort in Python"""
    length = len(arr)
    if reverse:
        for i in range(length-1):
            for j in range(length-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        for i in range(length-1):
                for j in range(length-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


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


def merge_sort(arr, reverse=False):
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
                if arr[left] >= arr[right]:
                    tmp_list.append(arr[right])
                    right += 1
                else:
                    tmp_list.append(arr[left])
                    left += 1
        else:
            while left < mid and right <= end:
                if arr[left] <= arr[right]:
                    tmp_list.append(arr[right])
                    right += 1
                else:
                    tmp_list.append(arr[left])
                    left += 1

        while left < mid:
            tmp_list.append(arr[left])
            left += 1

        while right <= end:
            tmp_list.append(arr[right])
            right += 1

        arr[start:end+1] = tmp_list

    divide(0, len(arr)-1)
    return arr


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


def radix_sort(arr, reverse=False):
    """Radix sort in Python

    This sort uses 'queue way'. But simply uses list in Python.
    Also it assumes all elements in arr are POSITIVE INTEGERS.
    """
    def get_nth_digit(n, d):
        n %= 10 ** d
        return n // 10 ** (d-1)

    digit = 0
    max_value = max(arr)
    while max_value:
        digit += 1
        max_value //= 10

    sort_queue = list()
    iter_range = range(10) if not reverse else range(9, -1, -1)

    for d in range(1, digit+1):
        for i in iter_range:
            for n in arr:
                if get_nth_digit(n, d) == i:
                    sort_queue.append(n)
        arr[:] = sort_queue.copy()  # Can you guess why assignment is like this?
        sort_queue.clear()
    return arr


def selection_sort(arr, reverse=False):
    """Selecetion sort in Python"""
    for i in range(len(arr)):
        tmp = i
        if not reversed:
            for j in range(i, len(arr)):
                if arr[tmp] > arr[j]:
                    tmp = j
        else:
            for j in range(i, len(arr)):
                if arr[tmp] < arr[j]:
                    tmp = j
        arr[tmp], arr[i] = arr[i], arr[tmp]
    return arr


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
