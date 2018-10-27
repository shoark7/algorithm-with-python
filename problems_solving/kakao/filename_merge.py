def is_a_first(a, b, names):

    def divide_name(name):
        i = 0
        head = num = tail = ''

        while not name[i].isnumeric():
            head += name[i]
            i += 1

        while name[i:i+1].isnumeric() and len(num) != 5:
            num += name[i]
            i += 1

        tail = name[i:]
        return head, num, tail

    a_parts = divide_name(a)
    b_parts = divide_name(b)

    # head
    if a_parts[0].upper() < b_parts[0].upper():
        return True
    elif a_parts[0].upper() > b_parts[0].upper():
        return False

    # num
    if int(a_parts[1]) < int(b_parts[1]):
        return True
    elif int(a_parts[1]) > int(b_parts[1]):
        return False

    # original order
    return names.index(a) < names.index(b)


def filename_merge(arr):
    arr_copy = arr.copy()

    def divide(lo, hi):
        if lo == hi:
            return arr_copy[lo]

        mid = (lo + hi) // 2
        divide(lo, mid)
        divide(mid+1, hi)

        merge(lo, mid, hi)

    def merge(lo, mid, hi):
        left = lo
        right = mid + 1
        tmp = []

        while left <= mid or right <= hi:
            if left <= mid and (right > hi or is_a_first(arr_copy[left], arr_copy[right], arr)):
                tmp.append(arr_copy[left])
                left += 1
            else:
                tmp.append(arr_copy[right])
                right += 1

        arr_copy[lo:hi+1] = tmp

    divide(0, len(arr_copy)-1)
    return arr_copy


if __name__ == '__main__':
    test = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
    print(test, '\n', filename_merge(test))

    print('\n' + '-' * 30 + '\n')

    test = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
    print(test, '\n', filename_merge(test))
