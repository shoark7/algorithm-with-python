"""Return ways to buy christams gifts for good children

:input:
1
6 4
1 2 3 4 5 6

:return:
3 1

url: https://algospot.com/judge/problem/read/CHRISTMAS
ID : CHRISTMAS
"""
def ways_buying(p_gifts, K):
    MOD = 20091101
    counter = [0 for _ in range(K)]
    ret = 0

    for i in range(len(p_gifts)):
        counter[p_gifts[i]] += 1

    for i in range(K):
        if counter[i] >= 2:
            ret = (ret + ((counter[i] * (counter[i] - 1)) // 2)) % MOD
    return ret


def max_buys(p_gifts, K):
    ret = [0 for _ in range(len(p_gifts))]
    prev = [-1 for _ in range(K)]

    for i in range(len(p_gifts)):
        if i > 0:
            ret[i] = ret[i-1]
        else:
            ret[i] = 0

        loc = prev[p_gifts[i]]
        if loc != -1:
            ret[i] = max(ret[i], ret[loc]+1)
        prev[p_gifts[i]] = i

    return ret[-1]


if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        N, K = (int(n) for n in input().split())
        gifts = [int(n) for n in input().split()]

        p_gifts = [0]
        for n in gifts:
            p_gifts.append((p_gifts[-1] + n) % K)

        print(ways_buying(p_gifts, K), max_buys(p_gifts, K))
