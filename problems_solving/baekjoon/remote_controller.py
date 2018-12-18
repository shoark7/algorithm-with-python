"""Get minimal number of turning to wanted channels

:input:
5457
3
6 7 8

:return:
6
"""
def min_clicks(N, channels, BASE=100):
    ret = abs(N - BASE)
    channels_cands = []
    N = str(N)
    l = len(N)

    def generate(i, tmp_str):
        nonlocal channels_cands
        if i == l:
            diff = abs(int(N) - int(tmp_str))
            channels_cands.append((diff + len(tmp_str), tmp_str))
            return

        t = N[i]
        if channels[int(t)]:
            generate(i+1, tmp_str+t)
            return

        d = 1
        going_on = True
        while going_on and d < 10:
            if int(t) + d < 10 and channels[int(t)+d]:
                generate(i+1, tmp_str+str(int(t)+d))
                going_on = False
            if int(t) - d >= 0 and channels[int(t)-d]:
                generate(i+1, tmp_str+str(int(t)-d))
                going_on = False
            d += 1

    channels_cands.sort()
    generate(0, '')
    return min(ret, channels_cands[0][0])


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    channels = [1 for _ in range(10)]
    for n in input().split():
        channels[int(n)] = 0

    print(min_clicks(N, channels))
