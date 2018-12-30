"""Implement permutation in Python"""


def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
