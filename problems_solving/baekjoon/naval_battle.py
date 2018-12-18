"""Return Ratio of right orders to all pairs

:input:
5
okpo sacheon hansan myeongnyang noryang
sacheon hansan myeongnyang noryang okpo

:return:
6/10

url: https://www.acmicpc.net/problem/3077
"""
def get_score(answers, submitted):
    N = len(answers)
    total_cand = int(N / 2 * (N - 1))
    ans = 0
    tmp_arr = [0] * N

    # tmp_arr[i] -> submitted 안에서 answers[i]가 있는 위치
    for i in range(N):
        target = answers[i]
        tmp_arr[i] = submitted.index(target)

    def find(chosen):
        nonlocal ans
        if len(chosen) == 2:
            a, b = chosen
            ans += (tmp_arr[a] < tmp_arr[b])
            return

        start = chosen[-1] + 1 if chosen else 0
        for nxt in range(start, N):
            chosen.append(nxt)
            find(chosen)
            chosen.pop()
    find([])
    return ans, int(total_cand)


if __name__ == '__main__':
    N = int(input())
    answers = [n for n in input().split()]
    submitted = [n for n in input().split()]
    n, total = get_score(answers, submitted)
    print(n, '/', total, sep='')
