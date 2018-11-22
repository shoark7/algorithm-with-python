"""Get the longest palindrome in a given string"""


def longest_palindrome(s: str) -> str:
    if not s:
        return 0

    N = len(s)
    cache = [[-1 for _ in range(N)] for _ in range(N)]
    ans = []

    def all_same(lo, hi):
        first = s[lo]
        for i in range(lo+1, hi+1):
            if s[i] != first:
                return False
        return True

    def get_len(lo, hi):
        if cache[lo][hi] != -1:
            return cache[lo][hi]
        elif lo == hi:
            return 1

        # first part
        add = lo
        if get_len(lo+1, hi) == hi - (lo+1) + 1 and all_same(lo+1, hi) and s[add] == s[lo+1]:
            pre_ret = get_len(lo+1, hi) + 1
        elif s[add] == s[hi] and get_len(lo+1, hi-1) == (hi-1) - (lo+1) + 1:
            pre_ret = get_len(lo+1, hi-1) + 2
        else:
            pre_ret = get_len(lo+1, hi)


        # latter part
        add = hi
        if get_len(lo, hi-1) == hi-1 - lo + 1 and all_same(lo, hi-1) and s[add] == s[hi-1]:
            suf_ret = get_len(lo, hi-1) + 1
        elif s[add] == s[lo] and get_len(lo+1, hi-1) == (hi-1) - (lo+1) + 1:
            suf_ret = get_len(lo+1, hi-1) + 2
        else:
            suf_ret = get_len(lo, hi-1)

        cache[lo][hi] = max(pre_ret, suf_ret)
        return cache[lo][hi]

    def longest_one():
        max_len = get_len(0, N-1)
        for h in range(N):
            for t in range(h, N):
                if get_len(h, t) == max_len and t - h + 1 == max_len:
                    ans.append(s[h:t+1])

        return ans

    return longest_one()
