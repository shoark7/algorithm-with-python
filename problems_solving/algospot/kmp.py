"""Implement KMP substring search algorithm"""
def inefficient_search(h, n):
    ans = 0
    pos = []
    for i in range(len(h)-len(n)+1):
        matched = True
        for j in range(len(n)):
            if h[i+j] != n[j]:
                matched = False
                break
        if matched:
            ans += 1
            pos.append(i)
    return ans, pos

# This simple algorithm works, but time complexity is O(|H| * |N|)
# '|X|' means length of X


# However, this algorithm, KMP can make it simple
def kmp_search(H, N):
    h_len, n_len = len(H), len(N)
    count, pos = 0, []
    begin, matched = 0, 0

    def generate_partial(N):
        begin, matched = 1, 0
        ret = [0] * (n_len+1)

        while begin + matched < n_len:
            if N[begin+matched] == N[matched]:
                matched += 1
                ret[begin+matched] = matched
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - ret[matched]
                    matched = ret[matched]
        return ret


    pi = generate_partial(N)

    while begin <= h_len - n_len:
        if matched < n_len and H[begin + matched] == N[matched]:
            matched += 1
            if matched == n_len:
                count += 1
                pos.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]

    return count, pos
