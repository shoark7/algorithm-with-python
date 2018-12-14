"""Return lengths of all possible names

:input:
ababcabababa
bcabab

:return:
2 4 9 18

url: https://algospot.com/judge/problem/read/NAMING
ID : NAMING
"""
def get_presuffix_len(s):
    N = len(s)
    ret = [0] * (N+1)
    begin, matched = 1, 0

    while begin + matched < N:
        if s[begin+matched] == s[matched]:
            matched += 1
            ret[begin+matched] = matched
        else:
            if not matched:
                begin += 1
            else:
                begin += matched - ret[matched]
                matched = ret[matched]
    return ret


def length_names(t):
    pi = get_presuffix_len(t)
    k = len(t)
    ans = []

    while k:
        ans.append(k)
        k = pi[k]

    ans.sort()
    return ans


if __name__ == '__main__':
    F = input()
    M = input()
    t = F + M
    ans = length_names(t)
    print(' '.join(str(c) for c in ans))
