"""Make smallest number of cases to make given N to 1

There are 3 rules for integer X to adapt.

1. if X is divisible by 3, divide it by 3.
2. if X is divisible by 2, divide it by 2.
3. Subtract 1.

When integer N is given, we wanna make it to 1 using 3 commands.
Get the smallest number of cases of it


if N = 10, answer is "3"  (10 -> 9 -> 3 -> 1)

url: https://www.acmicpc.net/problem/1463
"""
def make_to_1(n):
    cache = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        tmp = 987654321
        cache[i] = min(tmp, cache[i-1]+1)
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i//2]+1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i//3]+1)
    return cache[n]


if __name__ == '__main__':
    N = int(input())
    print(make_to_1(N))
