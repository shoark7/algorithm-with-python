"""Check if wildcard pattern matches the given string


ID: WILDCARD


https://algospot.com/judge/problem/read/WILDCARD
"""

# exhaustive search
def exhaustive_match(pattern: str, string: str):
    pos = 0
    while pos < len(pattern) and pos < len(string) and \
        (pattern[pos] == '?' or pattern[pos] == string[pos]):
        pos += 1

    if pos == len(pattern):
        return True if pos == len(string) else False

    if pattern[pos] == '*':
        skip = 0
        while skip + pos <= len(string):
            if exhaustive_match(pattern[pos+1:], string[pos+skip:]):
                return True
            skip += 1

    return False


# memoization
def memoized_match(pattern, word):
    len_p, len_w = len(pattern), len(word)
    cache = [[-1 for _ in range(len_w+1)] for _ in range(len_p+1)]
    def match(pp, wp):
        if cache[pp][wp] != -1:
            return cache[pp][wp]

        if pp < len_p and wp < len_w and (pattern[pp] == '?' or pattern[pp] == word[wp]):
            cache[pp][wp] = match(pp+1, wp+1)
            return cache[pp][wp]

        if pp == len_p:
            cache[pp][wp] = (wp == len_p)
            return cache[pp][wp]

        if pattern[pp] == '*':
            if match(pp+1, wp) or (wp < len_w and match(pp, wp+1)):
                cache[pp][wp] = True
                return True

        cache[pp][wp] = False
        return False

    return match(0, 0)
