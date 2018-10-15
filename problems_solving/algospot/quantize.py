"""Get the smallest sum of min error when arr and split size is given

ID  : QUANTIZE
url : https://algospot.com/judge/problem/read/QUANTIZE
"""
def get_smallest_minerror(arr, s):
    arr.sort()
    length = len(arr)
    cum_sum = [0 for _ in range(length)]
    cum_sq_sum = [0 for _ in range(length)]
    cum_sum[0] = arr[0]
    cum_sq_sum[0] = arr[0] * arr[0]
    cache = [[-1 for _ in range(s+1)] for _ in range(length+1)]

    for i in range(1, length):
        cum_sum[i] = cum_sum[i-1] + arr[i]
        cum_sq_sum[i] = cum_sq_sum[i-1] + arr[i] * arr[i]

    def min_error(lo, hi):
        p_sum = cum_sum[hi] - (cum_sum[lo-1] if lo != 0 else 0)
        p_sq_sum = cum_sq_sum[hi] - (cum_sq_sum[lo-1] if lo != 0 else 0)
        mean = round(p_sum / (hi - lo + 1))

        ret = p_sq_sum - 2 * mean * p_sum + mean * mean * (hi-lo+1)
        return ret

    def quantize(_from, parts):
        if _from == length:
            return 0
        if parts == 0:
            return 987654321
        if cache[_from][parts] != -1:
            return cache[_from][parts]

        ret = 987654321
        for part_size in range(1, length-_from+1):
            ret = min(ret, min_error(_from, _from+part_size-1) + quantize(_from + part_size,
                                                                          parts-1))
        cache[_from][parts] = ret
        return ret

    return quantize(0, s)


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N, S = (int(x) for x in input().split())
        arr = [int(n) for n in input().split()]
        ans.append(get_smallest_minerror(arr, S))

    for n in ans:
        print(n)
