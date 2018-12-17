"""Return length of shortest palindrome with given string

:input:
3
there
amanaplanacanal
xyz

:return:
7
21
5

url: https://algospot.com/judge/problem/read/PALINDROMIZE
ID : PALINDROMIZE
"""
from sys import stdin



def reverse(s):
    ret = ''
    N = len(s)
    for i in range(N):
        ret += s[N-1-i]
    return ret


def generate_partial(s):
    N = len(s)
    ret = [0] * (N+1)
    begin, matched = 1, 0

    while begin + matched < N:
        if s[begin + matched] == s[matched]:
            matched += 1
            ret[begin+matched] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - ret[matched]
                matched = ret[matched]
    return ret


def len_palindrome(s):
    rs = reverse(s)
    pi_rs = generate_partial(rs)
    N = len(s)
    begin = 0
    matched = 0
    rs_len = 0

    while begin + matched < N:
        if matched < N and s[begin + matched] == rs[matched]:
            matched += 1
            if begin + matched == N:
                rs_len = matched
                break
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi_rs[matched]
                matched = pi_rs[matched]

    return N * 2 - rs_len


if __name__ == '__main__':
    C = int(stdin.readline())
    ans = []
    for _ in range(C):
        word = stdin.readline().strip()
        ans.append(len_palindrome(word))

    for n in ans:
        print(n)
