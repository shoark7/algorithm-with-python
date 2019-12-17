from itertools import permutations


c_set = set()


def to_number(arr):
    ans = 0
    arr = arr[::-1]

    for i in range(len(arr)):
        ans *= 10
        ans += arr[i]

    return ans


for perm in permutations(range(1, 10)):
    for i in range(1, 3):
        a, b, c = perm[:i], perm[i:5], perm[5:]
        a, b, c = to_number(a), to_number(b), to_number(c)
        c = sorted(str(c))

        c_cand = a * b
        if sorted(str(c_cand)) == c and c_cand not in c_set:
            c_set.add(c_cand)


print(sum(c_set))
