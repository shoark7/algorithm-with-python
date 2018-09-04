"""Get the sequence of largest sum from an array of integers

This has several implementations and I look through it.

ID : MAXSUM

https://algospot.com/judge/problem/read/MAXSUM
"""
MIN = -100 - 1

# O(N^3) 
def inefficient_sum(arr):
    n, answer = len(arr), MIN
    for i in range(n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s += arr[k]
            answer = max(s, answer)
    answer = max(0, answer)
    return answer


# O(N ^ 2)
def better_sum(arr):
    n, answer = len(arr), MIN
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            answer = max(answer, s)
    answer = max(0, answer)
    return answer


# Divide & Conquer way : O(N*lnN)
def divide_conquer_sum(arr, lo, hi):
    if lo == hi:
        return arr[lo]

    mid = (lo + hi) // 2
    left, right = MIN, MIN
    s = 0

    for i in range(mid, lo-1, -1):
        s += arr[i]
        left = max(s, left)

    s = 0
    for j in range(mid+1, hi+1):
        s += arr[j]
        right = max(s, right)

    single = max(divide_conquer_sum(arr, lo, mid),
                 divide_conquer_sum(arr, mid+1, hi))

    return max(left + right, single, 0)


# Dynamic Programming : O(N)
def dynamic_sum(arr):
    psum = 0
    answer = MIN

    for n in arr:
        psum = max(psum, 0) + n
        answer = max(psum, answer)

    return max(answer, 0)





if __name__ == '__main__':
    t1 = [-7, 4, -3, 6, 3, -8, 3, 4]
    t2 = [1,2,3,4]
    t3 = [-3, -2, -1]

    assert 10 == inefficient_sum(t1)
    assert 10 == inefficient_sum(t2)
    assert 0 == inefficient_sum(t3)

    assert 10 == better_sum(t1)
    assert 10 == better_sum(t2)
    assert 0 == better_sum(t3)

    assert 10 == divide_conquer_sum(t1, 0, len(t1)-1)
    assert 10 == divide_conquer_sum(t2, 0, len(t2)-1)
    assert 0 == divide_conquer_sum(t3, 0, len(t3)-1)

    assert 10 == dynamic_sum(t1)
    assert 10 == dynamic_sum(t2)
    assert 0 == dynamic_sum(t3)

