"""Return the maximum differential of scores when 2 players play their best

:input:

3
5
-1000 -1000 -3 -1000 -1000
6
100 -1000 -1000 100 -1000 -1000
10
7 -5 8 5 1 -4 -8 6 7 9

:return:
-1000
1100
7

ID : NUMBERGAME
url: https://algospot.com/judge/problem/read/NUMBERGAME
"""
def score_diff(arr):
    length = len(arr)
    EMPTY = -987654321
    cache = [[EMPTY for _ in range(length)] for _ in range(length)]

    def play(left, right):
        if left > right:
            return 0
        elif cache[left][right] != EMPTY:
            return cache[left][right]
        ret = max(arr[left] - play(left+1, right),
                  arr[right] - play(left, right-1))

        if right - left + 1 >= 2:
            ret = max(ret, -play(left+2, right), -play(left, right-2))
        cache[left][right] = ret
        return ret

    return play(0, length-1)


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        input()
        arr = [int(n) for n in input().split()]
        ans.append(score_diff(arr))

    for n in ans:
        print(n)
