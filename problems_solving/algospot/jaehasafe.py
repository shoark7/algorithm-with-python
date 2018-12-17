"""Return least number of shifts to open safe

:input:
2
3
abbab
babab
ababb
bbaba
2
RMDCMRCD
MRCDRMDC
DCMRCDRM

:return:
6
10

url: https://algospot.com/judge/problem/read/JAEHASAFE
ID : JAEHASAFE
"""
def kmp_search(h, n):
    h_len, n_len = len(h), len(n)
    begin, matched = 0, 0
    pos = []

    def partial_match(s):
        begin, matched = 1, 0
        ret = [0] * (n_len + 1)
        while begin + matched < n_len:
            if s[begin+matched] == s[matched]:
                matched += 1
                ret[begin+matched] = matched
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - ret[matched]
                    matched = ret[matched]
        return ret

    pi = partial_match(n)
    while begin <= h_len - n_len:
        if matched < n_len and h[begin + matched] == n[matched]:
            matched += 1
            if matched == n_len:
                pos.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return pos


def jaehasafe(states):
    ans = 0
    right = True
    for i in range(len(states)-1):
        if right:
            ans += kmp_search(states[i+1] * 2, states[i])[0]
        else:
            ans += kmp_search(states[i] * 2, states[i+1])[0]
        right ^= True
    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        states = []
        N = int(input())
        for _ in range(N+1):
            states.append(input())
        ans.append(jaehasafe(states))
    for n in ans:
        print(n)
