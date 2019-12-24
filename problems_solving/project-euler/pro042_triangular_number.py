MAX_DELTA = 1000
CACHE = [1]
delta = 2

while delta <= MAX_DELTA:
    CACHE.append(CACHE[-1] + delta)
    delta += 1


def word_to_scala(word):
    BASE = ord('A') - 1
    return sum(ord(c) for c in word) - (BASE * len(word))


def is_triangular_number(n):
    global CACHE

    def search(lo, hi):
        if lo == hi:
            return n == CACHE[lo]

        mid = (lo + hi) // 2
        if n <= CACHE[mid]:
            return search(lo, mid)
        else:
            return search(mid+1, hi)

    return search(0, len(CACHE))


if __name__ == '__main__':
    words_text = open('./data042').read()
    words = words_text.replace(r'"', '').replace('\n', '').split(',')
    ans = 0

    for word in words:
        scala = word_to_scala(word)
        ans += is_triangular_number(scala)

    print(ans)
