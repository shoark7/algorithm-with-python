"""Get minimum cost of concatenating files

:input:
3
3
2 2 4
5
3 1 3 4 1
8
1 1 1 1 1 1 1 2

:return:
12
26
27

url: https://algospot.com/judge/problem/read/STRJOIN
ID : STRJOIN
"""
def strjoin(lens):
    ret = 0
    lens.sort()

    while len(lens) > 1:
        a = lens.pop(0)
        b = lens.pop(0)
        ret += a + b
        lens.append(a + b)
        lens.sort()
    return ret


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        lengths = [int(n) for n in input().split()]
        ans.append(strjoin(lengths))

    for n in ans:
        print(n)
