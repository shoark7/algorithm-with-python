"""Get the maximum area of the bars standing side by side

ID : FENCE

https://algospot.com/judge/problem/read/FENCE
"""
def solve(left: int, right: int):
    if left == right:
        return heights[left]

    mid = (left + right) // 2
    ans = max(solve(left, mid), solve(mid+1, right))

    lo, hi = mid, mid + 1
    height = min(heights[lo], heights[hi])
    ans = max(ans, height * 2)

    while left < lo or hi < right:
        if hi < right and (lo == left or heights[lo-1] < heights[hi+1]):
            hi += 1
            height = min(height, heights[hi])
        else:
            lo -= 1
            height = min(height, heights[lo])

        ans = max(ans, height * (hi - lo +1))

    return ans


C = int(input())
ans_list = []
for _ in range(C):
    input()
    heights = [int(x) for x in input().split()]
    ans_list.append(solve(0, len(heights)-1))

for n in ans_list:
    print(n)
