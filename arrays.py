def find_pair_with_given_sum_n2(a, s):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == s:
                return i, j
    return -1, -1


def find_pair_with_given_sum_n_logn(a, s):
    b = sorted(a)
    i = 0
    j = len(b) - 1

    while i < j:
        if b[i] + b[j] == s:
            return i, j
        elif b[i] + b[j] < s:
            i += 1
        elif b[i] + b[j] > s:
            j -= 1

    return -1, -1


def find_pair_with_given_sum_n(a, s):
    h = dict()

    for i in range(len(a)):
        if s - a[i] in h:
            return h[s - a[i]], i
        else:
            h[a[i]] = i

    return -1, -1


def check_if_subarray_with_sum_0_exists_n(a):
    h = {0}
    curr_sum = 0

    for x in a:
        curr_sum += x
        if curr_sum in h:
            return True
        h.add(curr_sum)

    return False


def return_all_subarrays_with_sum_0_n2(a):
    ans = []

    for i in range(len(a)):
        curr_sum = 0
        for j in range(i, len(a)):
            curr_sum += a[j]
            if curr_sum == 0:
                ans.append((i, j))

    return ans


def sort_binary_array_n(a):
    num_of_ones = 0

    for i in range(len(a)):
        if a[i] == 1:
            num_of_ones += 1
        a[i] = 0

    for i in range(-1, -num_of_ones - 1, -1):
        a[i] = 1

    return a


def find_duplicate_hashing_n_n(a):
    h = set()

    for x in a:
        if x in h:
            return x
        h.add(x)

    return -1


def find_duplicate_make_negative_n_1(a):
    for i in range(len(a)):
        curr = abs(a[i])

        if a[curr - 1] >= 0:
            a[curr - 1] = -a[curr - 1]
        else:
            return curr

    return -1


def find_duplicate_xor_n_1(a):
    xor = 0

    for x in a:
        xor ^= x

    for i in range(1, len(a)):
        xor ^= i

    if xor:
        return xor
    else:
        return -1


def find_duplicate_sum_difference_n_1(a):
    return sum(a) - sum(range(0, len(a)))


def find_max_length_subarray_of_given_sum_n2(a, s):
    max_length = 0
    ind = -1

    for i in range(len(a)):
        curr_sum = 0
        for j in range(i, len(a)):
            curr_sum += a[j]
            if curr_sum == s and max_length < j - i + 1:
                max_length = j - i + 1
                ind = j

    return a[ind - max_length + 1: ind + 1]


def find_max_length_subarray_of_given_sum_n(a, s):
    h = {}
    max_length = 0
    curr_sum = 0
    ind = -1

    for i in range(len(a)):
        curr_sum += a[i]
        if curr_sum not in h:
            h[curr_sum] = i

        if curr_sum - s in h and max_length < i - h[curr_sum - s]:
            max_length = i - h[curr_sum - s]
            ind = i

    return a[ind - max_length + 1: ind + 1]


