"""Multiply integers as we used to do in schools.

Time complexity is O(n ** 2)
"""
def multiply_integers(a: int, b: int):

    def process(a):
        if isinstance(a, int) and isinstance(b, int):
            a = [int(n) for n in reversed(str(a))]
        elif isinstance(a, list) and isinstance(b, list):
            a = int(''.join(reversed([str(c) for c in a])))
        else:
            raise TypeError("Two elements should be all integers or lists")
        return a


    def normalize(nums: list):
        nums.append(0)

        for i in range(len(nums)-1):
            if nums[i] < 0:
                borrow = (abs(nums[i]) + 9) // 10
                nums[i+1] -= borrow
                nums[i] += borrow * 10
            else:
                nums[i+1] += nums[i] // 10
                nums[i] %= 10

        while len(nums) > 1 and nums[-1] == 0:
            nums.pop()

        return nums


    def multiply(a: list, b: list):
        ans = [0 for _ in range(len(a) + len(b) + 1)]
        for i in range(len(a)):
            for j in range(len(b)):
                ans[i+j] += a[i] * b[j]

        return ans

    a = process(a)
    b = process(b)

    ans = multiply(a, b)
    ans = normalize(ans)
    ans = process(ans)

    return ans



if __name__ == '__main__':
    assert multiply_integers(1234, 5678) == 7006652
