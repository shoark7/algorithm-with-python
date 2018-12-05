"""Return number of primes between (n, 2n] when a natural number n is given

:input:
1
10
13
100
1000
10000
100000
0

:return:
1
4
3
21
135
1033
8392
"""
SIZE = 123456 * 2 + 1
SQRT_SIZE = int(SIZE ** (1/2))

sieves = [1 for _ in range(SIZE+1)]
sieves[0] = sieves[1] = 0
cum_count_prime = [0 for _ in range(SIZE+1)]


for n in range(2, SIZE+1):
    cum_count_prime[n] = cum_count_prime[n-1]
    if sieves[n] == 1:
        for j in range(n*n, SIZE+1, n):
            sieves[j] = 0

        cum_count_prime[n] += 1



if __name__ == '__main__':
    wanted = []
    while True:
        n = int(input())
        if n != 0:
            wanted.append(n)
        else:
            break

    for n in wanted:
        print(cum_count_prime[2*n] - cum_count_prime[n])
