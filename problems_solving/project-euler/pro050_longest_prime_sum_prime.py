if __name__ == '__main__':
    SIZE = 10 ** 6
    sieve = [1] * (SIZE + 1)
    sieve[1] = sieve[0] = 0

    for i in range(2, int(SIZE ** (1/2))+1):
        if sieve[i]:
            for j in range(i*i, SIZE+1, i):
                sieve[j] = 0

    primes = [i for i, n in enumerate(sieve) if n == 1]
    prime_set = set(primes)
    cum_primes = [0]

    for n in primes:
        cum_primes.append(cum_primes[-1] + n)


    length = 0
    ans = None

    for lo in range(1, len(cum_primes)):
        for hi in range(lo+length, len(cum_primes)):
            cum_sum = cum_primes[hi] - cum_primes[lo-1]
            if (cum_sum in prime_set) and (hi - lo + 1) > length:
                length = hi - lo + 1
                ans = cum_sum

            if cum_sum > SIZE:
                break
    print(ans)
