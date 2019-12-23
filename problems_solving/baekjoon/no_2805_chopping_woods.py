"""Get tallest height to chop off woods to get required lumber

url: https://www.acmicpc.net/problem/2805
"""
def get_tallest_heights(MIN_REQUIRED, heights):
    def lumber_got(height):
        ret = 0
        for h in heights:
            ret += max(0, h - height)

        return ret

    def get_height(lo, hi):
        if lo == hi:
            return lo

        mid = (lo + hi) // 2 + 1
        if lumber_got(mid) >= MIN_REQUIRED:
            return get_height(mid, hi)
        else:
            return get_height(lo, mid-1)

    return get_height(0, max(heights))


if __name__ == '__main__':
    _, MIN_REQUIRED = (int(n) for n in input().split())
    heights = [int(n) for n in input().split()]
    print(get_tallest_heights(MIN_REQUIRED, heights))
