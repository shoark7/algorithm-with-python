def create_pentagonal_list(size):
    ret = []
    for n in range(1, size+1):
        ret.append(n * (3*n - 1) // 2)

    return ret


if __name__ == '__main__':
    pentas = create_pentagonal_list(10000)
    penta_set = set(pentas)
    ans = float('inf')

    for i in range(len(pentas)):
        n1 = pentas[i]
        for j in range(i+1, len(pentas)):
            n2 = pentas[j]
            if (n1 + n2) in penta_set and (n2 - n1) in penta_set:
                ans = min(ans, n2 - n1)

    print(ans)
