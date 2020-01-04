"""Get maximum distances among routers along the straight line

url: https://www.acmicpc.net/problem/2110
"""
import sys

input = sys.stdin.readline


def count_installed_routers(locs, DIST):
    cnt = 1
    cur_loc = 0

    for l in range(1, len(locs)):
        if locs[l] - locs[cur_loc] >= DIST:
            cnt += 1
            cur_loc = l
    return cnt


def max_distances(locs, C, is_sorted=True):
    if not is_sorted:
        locs.sort()

    start = min(locs[i+1] - locs[i] for i in range(len(locs)-1))
    end = locs[-1] - locs[0]

    while start <= end:
        mid = (start + end) // 2
        installed_count = count_installed_routers(locs, mid)

        if installed_count < C:
            end = mid - 1
        elif installed_count >= C:
            ans = mid
            start = mid + 1

    return ans


if __name__ == '__main__':
    N, C = (int(n) for n in input().split())
    locs = []

    for _ in range(N):
        locs.append(int(input()))

    locs.sort()
    print(max_distances(locs, C))
