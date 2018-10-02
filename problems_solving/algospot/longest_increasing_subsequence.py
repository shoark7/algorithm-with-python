"""Get the length of longest increasing subsequence


url : https://algospot.com/judge/problem/read/LIS
ID  : LIS
"""


# In exhaustive search
def lis_all(arr):
    if len(arr) == 0:
        return 0
    ret = 0
    for i in range(len(arr)):
        tmp = []
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                tmp.append(arr[j])
        ret = max(ret, 1+lis(tmp))
    return tmp


# In dynamic programming
def lis(arr):
    arr = [-1] + arr
    cache = [-1 for _ in range(len(arr))]
    ans = -1

    def search(start):
        if cache[start] != -1:
            return cache[start]
        cache[start] = 1
        for i in range(start+1, len(arr)):
            if arr[start] < arr[i]:
                cache[start] = max(cache[start], search(i)+1)
        return cache[start]

    return search(0) - 1


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        input()
        arr = [int(n) for n in input().split()]
        ans.append(lis(arr))

    for n in ans:
        print(n)
