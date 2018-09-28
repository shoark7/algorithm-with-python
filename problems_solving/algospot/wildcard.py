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
def memoized_match(pattern, string):
    len_p, len_s = len(pattern), len(string)
    cache = [[-1 for _ in range(len_s+1)] for _ in range(len_p+1)]

    def match(p, s):
        if cache[p][s] != -1:
            return cache[p][s]

        while p < len_p and s < len_s and (pattern[p] == '?' or pattern[p] == string[s]):
            cache[p][s] = match(p+1, s+1)
            return cache[p][s]

        if p == len_p:
            cache[p][s] = (s == len_s)
            return cache[p][s]

        if pattern[p] == '*':
            if match(p+1, s) or (s < len_s and  match(p, s+1)):
                cache[p][s] = True
                return True
        return False

    return match(0, 0)
