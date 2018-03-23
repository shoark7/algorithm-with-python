"""
2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두
6가지가 있습니다 (거슬러 가지는 않기로 합니다).


그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?
"""


def factorial(n, _cache={1:1, 2:2}):
    if n in _cache:
        return _cache[n]
    else:
        value = n * factorial(n-1)
        _cache[n] = value
        return value


def way_lattice(nth):
    return factorial(2 * nth) // factorial(nth) // factorial(nth)


print(way_lattice(20))

