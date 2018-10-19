"""Get ways to cover the board which is asymmetric from left to right

:input:
3
2
4
92

:return:
0
2
913227494
"""
MAX_T = 100
MOD = 1000000007
cache = [0 for _ in range(MAX_T+1)]
cache[0] = 1
cache[1] = 1
cache[2] = 2


for i in range(3, MAX_T+1):
    cache[i] = (cache[i-1] + cache[i-2]) % MOD

def asym_tile(n):
    if n % 2 == 1:
        ans = (cache[n] - cache[n//2] + MOD) % MOD
    else:
        ans = (cache[n] - cache[n//2] - cache[n//2 - 1] + MOD) % MOD

    return ans


if __name__ == '__main__':
    ans = []
    C = int(input())
    for _ in range(C):
        ans.append( asym_tile(int(input())))

    for n in ans:
        print(n)
