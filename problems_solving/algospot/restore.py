"""Get a joined string of shortest length from strings

:input:
3
3
geo
oji
jing
2
world
hello
3
abrac
cadabra
dabr

:return:
geojing
helloworld
cadabrac


url : https://algospot.com/judge/problem/read/RESTORE
ID  : RESTORE
"""
def shortest_length(strs):
    strs = list(set(strs))
    subsets = []
    for i in range(len(strs)):
        for j in range(len(strs)):
            if i == j:
                continue
            if strs[i] in strs[j]:
                subsets.append(strs[i])

    strs = [strs[i] for i in range(len(strs)) if strs[i] not in subsets]


    ans = sum(len(s) for s in strs)
    length = len(strs)
    cache = [[-1 for _ in range(1<<length)] for _ in range(length)]
    overlaps = [[0 for _ in range(length)] for _ in range(length)]
    ALL_USED = (1<<length) - 1

    def shared(prefix, suffix):
        i = 0
        MAX_I = min(len(prefix), len(suffix))
        ret = 0
        while i < MAX_I:
            if prefix[-(i+1):] == suffix[:i+1]:
                ret = i + 1
            i += 1
        return ret

    for prev in range(length):
        for nxt in range(length):
            overlaps[prev][nxt] = shared(strs[prev], strs[nxt])


    def get_max_dupl(last, used):
        if used == ALL_USED:
            return 0
        if cache[last][used] != -1:
            return cache[last][used]

        ret = 0
        for nxt in range(length):
            if used & (1<<nxt) == 0:
                cand = overlaps[last][nxt] + get_max_dupl(nxt, used + (1<<nxt))
                ret = max(ret, cand)

        cache[last][used] = ret
        return ret

    def reconstruct(last, used):
        if used == ALL_USED:
            return ''
        for nxt in range(length):
            if used & (1<<nxt):
                continue
            if_used = get_max_dupl(nxt, used + (1<<nxt)) + overlaps[last][nxt]
            if get_max_dupl(last, used) == if_used:
                return strs[nxt][overlaps[last][nxt]:] + reconstruct(nxt, used+(1<<nxt))

        return "There's something going on, anywhere I go tonight, tonight, tonight"

    ans = '-' * (ans+1)
    for i in range(length):
        tmp = strs[i] + reconstruct(i, 1<<i)
        if len(tmp) < len(ans):
            ans = tmp
    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []
    i = 0
    for _ in range(C):
        n = int(input())
        strs = []
        for _ in range(n):
            strs.append(input())
        ans.append(shortest_length(strs))

    for n in ans:
        print(n)
