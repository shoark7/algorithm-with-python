"""Return number of connected subsequences that sum up to K

:input:
3
8791 20
5265 5000
3578452 5000000

:return:
1
4
1049

url: https://algospot.com/judge/problem/read/ITES
ID : ITES
"""
# Unefficient offline solution 
def offline_solution(signals, k):
    ret = 0
    N = len(signals)

    for s in range(N):
        tmp_sum = 0
        for e in range(s, N):
            tmp_sum += signals[e]
            if tmp_sum == k:
                ret += 1
            if tmp_sum >= k:
                break
    return ret


class Queue:
    def __init__(self, arr=[]):
        self._len = len(arr)
        self._queue = list(arr)

    def is_empty(self):
        return self._len == 0

    def pop(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        self._len -= 1
        return self._queue.pop(0)

    def push(self, v):
        self._len += 1
        self._queue.append(v)




def signal_generator(N):
    seed = 1983
    for _ in range(N):
        yield seed % 10000 + 1
        seed = (seed * 214013 + 2531011) % (2 ** 32)


# It goes down to better solution below
def optimized_solution(N, k):
    ret, tail = 0, 0
    tmp_sum = 0
    queue = Queue()
    generator = signal_generator(N)

    for i in range(N):
        new_signal = next(generator)
        tmp_sum += new_signal
        queue.push(new_signal)

        while tmp_sum > k:
            tmp_sum -= queue.pop()

        if tmp_sum == k:
            ret += 1
    return ret


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        K, N = (int(n) for n in input().split())
        ans.append(optimized_solution(N, K))

    for n in ans:
        print(n)
