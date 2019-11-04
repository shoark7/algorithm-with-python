"""Get (A ** B) % C in an effective way

url: https://www.acmicpc.net/problem/1629
"""
def multiplication(iterable):
    A, B, C = iterable

    e = 0
    ans = 1
    tmp = A % C

    while 2 ** e <= B:
        if (2 ** e) & B != 0:
            ans = (ans * tmp) % C

        tmp = (tmp * tmp) % C
        e += 1

    return ans


if __name__ == '__main__':
    print(multiplication(int(n) for n in input().split()))
