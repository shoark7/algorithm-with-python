"""Get length of LIS in a sequence

url: https://www.acmicpc.net/problem/12015
"""
def length_of_lis(arr):
    tmp_lis = []
    length = 0

    for n in arr:
        if not tmp_lis or tmp_lis[-1] < n:
            tmp_lis.append(n)
            length += 1
        else:
            lo, hi = 0, length - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if n <= tmp_lis[mid]:
                    hi = mid
                else:
                    lo = mid + 1

            tmp_lis[lo] = n

    return length


if __name__ == '__main__':
    input()
    arr = [int(n) for n in input().split()]
    print(length_of_lis(arr))
