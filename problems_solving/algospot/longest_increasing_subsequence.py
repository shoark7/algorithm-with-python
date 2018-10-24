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
        ret = max(ret, 1+lis_all(tmp))
    return ret


# In dynamic programming
def lis(arr):
    arr = [-1] + arr
    cache = [-1 for _ in range(len(arr))]

    def search(start):
        if cache[start] != -1:
            return cache[start]
        ret = 1
        for i in range(start+1, len(arr)):
            if arr[start] < arr[i]:
                ret = max(ret, search(i)+1)
        cache[start] = ret
        return cache[start]

    return search(0) - 1


# Get the lis itself, not the length of it(Actually we need this, aren't we?)
def get_real_lis(arr):
    arr = [-1] + arr
    length = len(arr)
    cache = [-1 for _ in range(length)]
    choices = [-1 for _ in range(500)]
    ans = []

    def find(start):
        if cache[start] != -1:
            return 1
        ret = 1
        best_next = -1

        for i in range(start+1, length):
            if arr[start] < arr[i]:
                cand = find(i) + 1
                if cand > ret:
                    ret = cand
                    best_next = i
        choices[start+1] = best_next
        return ret

    def reconstruct(start, ans_arr):
        if choices[start] != -1:
            ans_arr.append(arr[start])
        nxt = choices[start+1]
        if nxt != -1:
            reconstruct(nxt, ans_arr)

    find(0)
    reconstruct(0, ans)
    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []
    arrs = []
    for i in range(C):
        input()
        arrs.append([int(n) for n in input().split()])
        ans.append(get_real_lis(arrs[i]))


    for i in range(len(ans)):
        print(arrs[i], ans[i])
