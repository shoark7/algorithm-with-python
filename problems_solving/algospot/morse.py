"""Get the k th Morse code when number of 'o' and '-' are given

:input:
3
2 2 4
4 8 13
6 4 1

:return:
o--o
--o-ooo-oooo
------oooo

ID : MORSE
url: https://algospot.com/judge/problem/read/MORSE
"""
# Exhaustive search
def morse(n, m, k):
    skip = k - 1
    ans = ''

    def generate(n, m, s):
        nonlocal skip, ans
        if skip < 0:
            return
        if n == 0 and m == 0:
            if skip == 0:
                ans = s
            skip -= 1
            return
        if n > 0:
            generate(n-1, m, s+'-')
        if m > 0:
            generate(n, m-1, s+'o')

    generate(n, m, '')
    return ans


# Dynamic programming
def morse_dp(n, m, k):
    t = n + m
    cache = [[0 for _ in range(t+1)] for _ in range(t+1)]
    ans = ''
    skip = k - 1

    for i in range(t+1):
        cache[i][i] = cache[i][0] = 1

    for i in range(1, t+1):
        for j in range(1, t+1):
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

    def generate(n, m, s):
        nonlocal skip, ans

        if skip < 0:
            return
        if n == 0 and m == 0:
            if skip == 0:
                ans = s
            skip -= 1
            return
        if cache[n+m][n] <= skip:
            skip -= cache[n+m][n]
            return
        if n > 0:
            generate(n-1, m, s+'-')
        if m > 0:
            generate(n, m-1, s+'o')

    generate(n, m, '')
    return ans


# Optimized final version
def morse_final(n, m, k):
    t = n + m
    cache = [[0 for _ in range(t+1)] for _ in range(t+1)]
    skip = k - 1

    for i in range(t+1):
        cache[i][i] = cache[i][0] = 1

    for i in range(1, t+1):
        for j in range(1, t+1):
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

    def kth(n, m, skip):
        if n == 0:
            return m * 'o'
        if skip < cache[n+m-1][n-1]:
            return '-' + kth(n-1, m, skip)
        else:
            return 'o' + kth(n, m-1, skip - cache[n+m-1][n-1])

    return kth(n, m, skip)



if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        n, m, k = (int(x) for x in input().split())
        ans.append(morse_final(n, m, k))

    for m in ans:
        print(m)
