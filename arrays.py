import sys
import itertools

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


def find_maximum_product_of_two_elements_in_array_n2(a):
    max_prod = -sys.maxsize

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            if a[i] * a[j] > max_prod:
                max_prod = a[i] * a[j]

    return max_prod


def find_maximum_product_of_two_elements_in_array_nlogn(a):
    b = sorted(a)

    if b[0] * b[1] > b[-1] * b[-2]:
        return b[0] * b[1]
    else:
        return b[-1] * b[-2]


def find_maximum_product_of_two_elements_in_array_n(a):
    max_val = -sys.maxsize
    max2_val = -sys.maxsize
    min_val = sys.maxsize
    min2_val = sys.maxsize

    for x in a:
        if x > max_val:
            max2_val = max_val
            max_val = x
        elif x > max2_val:
            max2_val = x

        if x < min_val:
            min2_val = min_val
            min_val = x
        elif x < min2_val:
            min2_val = x

    if max_val * max2_val > min_val * min2_val:
        return max_val * max2_val
    else:
        return min_val * min2_val


def dutch_national_flag_problem_n(a):
    l = 0
    m = 0
    h = len(a) - 1
    pivot = 1

    while m <= h:
        if a[m] > pivot:
            a[m], a[h] = a[h], a[m]
            h -= 1
        elif a[m] < pivot:
            a[m], a[l] = a[l], a[m]
            l += 1
            m += 1
        else:
            m += 1

    return a


def merge_two_sorted_arrays_in_place_mn(a, b):
    for i in range(len(a)):
        if a[i] > b[0]:
            a[i], b[0] = b[0], a[i]
            tmp = b[0]
            k = 1
            while k < len(b) and b[k] < tmp:
                b[k - 1] = b[k]
                k = k + 1
            b[k - 1] = tmp

    return a, b


def merge_two_arrays_one_containing_vacant_zeros_mn(a, b):
    k = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[k] = a[i]
            a[i] = 0
            k = k + 1

    t = len(a) - 1
    k = k - 1
    n = len(b) - 1

    while k >= 0 and n >= 0:
        if a[k] > b[n]:
            a[t] = a[k]
            k -= 1
        else:
            a[t] = b[n]
            n -= 1

        t -= 1

    while n >= 0:
        a[t] = b[n]
        t -= 1
        n -= 1

    return a


def index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(a):
    zero = -1
    max_zero = -1
    curr_subarray = 0
    max_subarray = 0

    for i in range(len(a)):
        if a[i] == 1:
            curr_subarray += 1
        else:
            curr_subarray = i - zero - 1
            zero = i

        if curr_subarray > max_subarray:
            max_subarray = curr_subarray
            max_zero = zero

    return max_zero


def fisher_yates_shuffle_n(a):
    import random

    for i in range(len(a) - 1, 0, -1):
        j = random.randint(0, i)
        a[i], a[j] = a[j], a[i]

    return a


def every_second_element_greater_than_its_neighbours_n(a):
    for i in range(1, len(a), 2):
        if a[i - 1] > a[i]:
            a[i - 1], a[i] = a[i], a[i - 1]

        if i + 1 < len(a) and a[i] < a[i + 1]:
            a[i + 1], a[i] = a[i], a[i + 1]

    return a


def find_equilibrium_index_of_an_array_n(a):
    prefix_sums = list(itertools.accumulate(a))
    ans = list()

    for i in range(len(a)):
        left = prefix_sums[i - 1]
        right = prefix_sums[-1]

        if i == 0:
            left = 0
        elif i + 1 == len(a):
            right = 0

        if left == right - left - a[i]:
            ans.append(i)

    return tuple(ans)


def find_longest_consecutive_subarray_n_logn(a):
    b = sorted(a)
    max_ind = 1
    curr_len = 1
    max_len = 1

    for i in range(1, len(b)):
        if b[i] - b[i - 1] <= 1:
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
                max_ind = i
        else:
            curr_len = 1

    return b[max_ind - max_len + 1: max_ind + 1]


def boyer_moore_n_n(a):
    frequency = dict()

    for x in a:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1

    threshold = len(a) / 2

    for k in frequency:
        if frequency[k] > threshold:
            return k

    return None
