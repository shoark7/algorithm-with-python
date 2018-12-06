"""Implement sieve of Eratosthenes in BITMASK version

OMG... There are so many geeks around the world.
When the size of the sieve is too big like over billion,
then you can consider making a sieve with bitmask.

So let's get down to code directly...
"""
SIZE = 2 ** 16 + 1 # Size is too big... Isn't it?


class Sieve:
    def __init__(self, size):
        self._size = size
        self._sieve = [255 for _ in range(SIZE // 8 + 1)]

        self._set_composite(0)
        self._set_composite(1)

        for i in range(2, int(self._size ** (1/2))+1):
            for j in range(i*i, self._size+1, i):
                self._set_composite(j)
        print(f"Sieve of size {size} is initialized")


    def is_prime(self, n):
        if n > self._size:
            raise ValueError(f"This sieve only support integers equal to or less than {self._size}")
        return True if self._sieve[n >> 3] & (1 << (n & 7)) else False

    def _set_composite(self, n):
        self._sieve[n >> 3] &= ~(1 << (n & 7))
