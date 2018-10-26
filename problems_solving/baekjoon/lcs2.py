"""Get LCS in two sentences

:input:
ACAYKP
CAPCAK

:return:
4
ACAK

url: https://www.acmicpc.net/problem/9252
"""
def lcs_exhaustive(a, b):
    if a == '' or b == '':
        return ''
    ret = ''
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                cand = a[i] + lcs_exhaustive(a[i+1:], b[j+1:])
                ret = ret if len(ret) >= len(cand) else cand
    return ret


def lcs(a, b):
    a = ' ' + a
    b = ' ' + b
    cache = [[0 for _ in range(len(b))] for _ in range(len(a))]
    lcs_cache = [['' for _ in range(len(b))] for _ in range(len(a))]

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                cache[i][j] = cache[i-1][j-1] + 1
                lcs_cache[i][j] = lcs_cache[i-1][j-1] + a[i]
            elif cache[i-1][j] > cache[i][j-1]:
                cache[i][j] = cache[i-1][j]
                lcs_cache[i][j] = lcs_cache[i-1][j]
            else:
                cache[i][j] = cache[i][j-1]
                lcs_cache[i][j] = lcs_cache[i][j-1]
    return lcs_cache[len(a)-1][len(b)-1]


if __name__ == '__main__':
    a = input()
    b = input()
    ans = lcs(a, b)
    print(len(ans))
    print(ans)
