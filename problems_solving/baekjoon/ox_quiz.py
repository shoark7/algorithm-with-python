"""Get total score in a given OX string

:input:
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

:output:
10
9
7
55
30

ID  : OX quiz
url : https://www.acmicpc.net/problem/8958
"""
def sum_from(n, _from=0):
    return _from if n == _from else n + sum_from(n-1, _from)


def get_total_score(ox):
    ox = 'X' + ox + 'X'
    last = 0
    score = 0
    for i in range(1, len(ox)):
        if ox[i] == 'X':
            count = i - last - 1
            score += sum_from(count)
            last = i
    return score


if __name__ == '__main__':
    N = int(input())
    oxs = []
    for _ in range(N):
        oxs.append(get_total_score(input()))

    for n in oxs:
        print(n)
