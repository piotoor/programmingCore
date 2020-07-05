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
