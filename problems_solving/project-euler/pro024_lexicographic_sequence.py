from math import factorial


def get_nth_sequence(sequence, nth):
    S = len(sequence)

    if factorial(S) < nth:
        return -1

    nth -= 1
    used = [0] * S
    sequence = list(sequence)
    ret = ''

    for i in range(1, S+1):
        count = 0
        while nth >= factorial(S - i):
            count += 1
            nth -= factorial(S - i)

        for j in range(S):
            if not used[j]:
                if count != 0:
                    count -= 1
                else:
                    use_this = j
                    break
        used[use_this] = 1
        ret += str(sequence[use_this])

    return ret
