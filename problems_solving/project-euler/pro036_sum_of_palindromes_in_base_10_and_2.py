def is_palindrome_str(strng):
    if len(strng) <= 1:
        return True

    return False if strng[0] != strng[-1] else is_palindrome_str(strng[1:-1])


if __name__ == '__main__':
    SIZE = 10 ** 6
    ret = 0

    for n in range(1, SIZE+1):
        bin_n = bin(n)[2:]

        if is_palindrome_str(bin_n) & is_palindrome_str(str(n)):
            ret += n

    print(n)
