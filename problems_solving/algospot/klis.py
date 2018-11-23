"""Get the kth Longest Increasing Subsequence

:input:
3
9 2
1 9 7 4 2 6 3 11 10
8 4
2 1 4 3 6 5 8 7
8 2
5 6 7 8 1 2 3 4

:return:
4
1 2 3 11
4
1 3 6 8
4
5 6 7 8


url: https://algospot.com/judge/problem/read/KLIS
ID : KLIS
"""
def klis(arr, k):
    N = len(arr)
    len_cache = [-1 for _ in range(N+1)]
    cnt_cache = [-1 for _ in range(N+1)]
    ans = []
    skip = k - 1

    def l(i):
        if i == N:
            return 0
        elif len_cache[i+1] != -1:
            return len_cache[i+1]

        ret = 1
        for x in range(i+1, N):
            if i == -1 or arr[i] < arr[x]:
                ret = max(ret, 1+l(x))
        len_cache[i+1] = ret
        return ret

    def cnt(i):
        if l(i) == 1:
            return 1
        elif cnt_cache[i+1] != -1:
            return cnt_cache[i+1]
        ret = 0
        for nxt in range(i+1, N):
            if (i == -1 or arr[i] < arr[nxt]) and l(i) == l(nxt) + 1:
                ret += cnt(nxt)

        cnt_cache[i+1] = ret
        return ret

    def reconstruct(start, skip, lis):
        if start != -1:
            lis.append(arr[start])

        cand = []
        for nxt in range(start+1, N):
            if (start == -1 or arr[start] < arr[nxt]) and l(start) == l(nxt) + 1:
                cand.append((arr[nxt], nxt))
        cand.sort()

        for v, i in cand:
            count = cnt(i)
            if count <= skip:
                skip -= count
            else:
                reconstruct(i, skip, lis)
                break

    reconstruct(-1, skip, ans)
    return l(-1) -1, ans


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, K = (int(n) for n in input().split())
        seq = [int(n) for n in input().split()]
        ans.append(klis(seq, K))

    for n, lis in ans:
        print(n)
        print(' '.join(str(x) for x in lis))
