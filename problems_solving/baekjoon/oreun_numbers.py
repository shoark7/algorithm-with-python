"""Get the right most large numbers from array

url: https://www.acmicpc.net/problem/17298
"""
def get_oreun_numbers(nums):
    stack = []
    ans = [-1] * len(nums)

    for i, n in enumerate(nums):
        while stack:
            prev_i, prev_n = stack[-1]
            if prev_n < n:
                stack.pop()
                ans[prev_i] = n
            else:
                break

        stack.append((i, n))

    return ans


if __name__ == '__main__':
    _ = int(input())
    arr = [int(n) for n in input().split()]
    print(' '.join(str(n) for n in get_oreun_numbers(arr)))
