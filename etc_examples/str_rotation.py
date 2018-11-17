# 1. pull each one
def rotate_modulo(s, m):
    if m <= 0 or not s:
        return s
    elif m >= len(s):
        return rotate_modulo(s, m % len(s))

    n = len(s)
    new = ['' for _ in range(n)]
    for i in range(n):
        new[(i-m) % n] = s[i]
    return ''.join(new)


# 2. Use string reverse formula
def rotate_reverse(s, m):
    if m <= 0 or not s:
        return s
    elif m >= len(s):
        return rotate_reverse(s, m % len(s))

    def reverse(s):
        length = len(s)
        new = ['' for _ in range(length)]
        for i in range(length):
            new[length-1-i] = s[i]

        return ''.join(new)

    h = t = ''
    for i in range(m):
        h += s[i]

    for i in range(m, len(s)):
        t += s[i]

    return reverse(reverse(h) + reverse(t))


# 3. Use one cache variable
def rotate_shell(s, m):
    if m <= 0 or not s:
        return s
    elif m >= len(s):
        return rotate_shell(s, m % len(s))

    length = len(s)
    new = ['' for _ in range(length)]
    tmp = new[0]
    to = 0
    for i in range(length-1):
        _from = (to + m) % length
        new[to] = s[_from]
        to = _from

    new[to] = tmp
    return ''.join(new)


# 4. Use Divide and Conquer
def rotate_divide(s, m):
    if m <= 0 or not s:
        return s
    elif m >= len(s):
        return rotate_divide(s, m % len(s))

    s = [c for c in s]
    def change(s, hs, ts, n):
        tmp = ['' for _ in range(n)]
        for i in range(n):
            tmp[i] = s[hs+i]
            s[hs+i] = s[ts+i]
            s[ts+i] = tmp[i]

    def rotate(lo, hi, m):
        n = hi - lo + 1
        if n % 2 == 0 and n // 2 == m:
            change(s, lo, lo+m, m)
        elif m < n - m:
            change(s, lo, hi-m+1, m)
            rotate(lo, hi-m, m)
        else:
            m = n - m
            change(s, lo, hi-m+1, m)
            rotate(lo+m, hi, n-2 * m)

    rotate(0, len(s)-1, m)
    return ''.join(s)


if __name__ == '__main__':
    s = 'zzz12123asdfasdf'
    print('modulo rotation', rotate_modulo(s, 3))
    print('reverse rotation', rotate_reverse(s, 3))
    print('shell rotation', rotate_shell(s, 3))
    print('divide & conquer rotation', rotate_divide(s, 3))
