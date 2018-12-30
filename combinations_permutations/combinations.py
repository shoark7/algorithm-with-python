"""Combinations without replacements in Python


Source referred in Python org.
Last Modified Date: 2018/12/30
"""
def combination(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

