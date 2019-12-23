def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for d in range(3, int(n ** (1/2))+1, 2):
        if n % d == 0:
            return False

    return True


def permutations(digit):
    used = [0] * (digit + 1)
    used[0] = 1
    all_nums = []

    def generate(tmp, used):
        nonlocal all_nums
        if all(used):
            all_nums.append(tmp)

        for n in range(1, digit+1):
            if not used[n]:
                used[n] = 1
                generate(tmp * 10 + n, used)
                used[n] = 0

    generate(0, used)
    return all_nums


if __name__ == "__main__":
    found = False
    largest = -1

    for l in range(9, 0, -1):
        all_nums = permutations(l)
        for n in all_nums:
            if is_prime(n) and largest < n:
                largest = n
                found = True

        if found:
            break

    print(largest)
