"""Get the least sum of difficulties of memorizing pi with given string


url: https://algospot.com/judge/problem/read/PI
ID : PI
"""
INF = 987654321


def is_all_same(number):
    n = number[0]
    return all(n == x for x in number)


def is_monotonous(number, by=None):
    if by is None:
        by = int(number[1]) - int(number[0])

    if len(number) == 1:
        return True

    for i in range(len(number)-1):
        if int(number[i+1]) - int(number[i]) != by:
            return False
    return True


def is_one_by_one(number):
    if len(number) == 1:
        return True

    length = len(number)
    even = number[0]
    odd = number[1]

    for i in range(length // 2):
        if number[2*i] != even or number[2*i+1] != odd:
            return False

    if length % 2 == 1:
        if number[length-1] != even:
            return False

    return True


def get_difficulty(number):
    if is_all_same(number):
        return 1
    elif is_monotonous(number, 1):
        return 2
    elif is_one_by_one(number):
        return 4
    elif is_monotonous(number):
        return 5
    else:
        return 10


def least_difficulty(N):
    N = str(N).strip()
    length = len(N)
    cache = [-1 for _ in range(length)]

    def calculate(begin):
        ret = INF

        if begin == length:
            return 0
        elif cache[begin] != -1:
            return cache[begin]

        for l in range(3, 5+1):
            if begin + l <= length:
                ret = min(ret, calculate(begin+l) + get_difficulty(N[begin:begin+l]))

        cache[begin] = ret
        return ret

    return calculate(0)


if __name__ =='__main__':
    C = int(input())
    ans_list = []
    for _ in range(C):
        ans_list.append(least_difficulty(input()))

    for n in ans_list:
        print(n)
