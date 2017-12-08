def binary_search(value, target, reverse=False, changed=False):
    if value not in target:
        return -1

    if changed:
        target.sort(reverse=reverse)
    else:
        ordered = sorted(target, reverse=reverse)

    def search(start, end):
        mid = (start + end) // 2
        if value > ordered[mid]:
            return search(mid, end)
        elif value < ordered[mid]:
            return search(start, mid)
        else:
            return mid

    return search(0, ordered[len(ordered)-1])
