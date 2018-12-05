"""Get denominator of last element of henry expression

:input:
3
4 23
5 7
8 11

:return:
138
70
4070

url: https://www.acmicpc.net/problem/10253
"""
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def get_last_denominator(a, b):
    while a != 1:
        denom = int(b / a + 1)
        a = a * denom - b
        b *= denom

        a //= gcd(a, b)
        b //= gcd(a, b)

    return b


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        a, b = (int(n) for n in input().split())
        ans.append(get_last_denominator(a, b))

    for n in ans:
        print(n)
