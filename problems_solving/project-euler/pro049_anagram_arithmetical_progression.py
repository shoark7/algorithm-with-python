def are_anagrams(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


if __name__ == '__main__':
    ans = []
    sieve = [1] * (10000 + 1)
    sieve[0] = sieve[1] = 0

    for i in range(2, int(10000 ** (1/2))+1):
        if sieve[i]:
            for j in range(i*i, 10000+1, i):
                sieve[j] = 0


    for n in range(1000, 10000):
        d = 1
        while n + 2 * d < 10000:
            if sieve[n] and sieve[n + d] and sieve[n + 2 * d] \
               and are_anagrams(n, n + d) and are_anagrams(n + 2 * d, n):
                ans.append((n, n + d, n + 2 * d))
            d += 1

    print(ans)
