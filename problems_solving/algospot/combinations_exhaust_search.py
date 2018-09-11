"""Get all possible number of cases when n and r are given

There are various ways to get combinations.
Here, I implement with exhaust search(Brute force)
"""
def combinations(n, r, filled=None):
    if r > n:
        raise ValueError("r can't be greater than n")
    if r == 0:
        print(filled)
        return
    filled = filled if filled else []
    smallest = 0 if not filled else filled[-1] + 1

    for nxt in range(smallest, n):
        filled.append(nxt)
        combinations(n, r-1, filled)
        filled.pop()


if __name__ == '__main__':
    combinations(10, 3)
    combinations(1, 1)
