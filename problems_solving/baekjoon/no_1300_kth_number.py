"""Get kth number

url: https://www.acmicpc.net/problem/1300
"""
def kth_number(N, K):
    left, right = 1, K

    while left <= right:
        cnt = 0
        mid = (left + right) // 2

        for d in range(1, N+1):
            cnt += min(mid // d, N)

        if cnt < K:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1

    return ans


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    print(kth_number(N, K))
