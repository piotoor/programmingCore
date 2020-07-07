import unittest
import arrays


class TestFindPairWithGivenSum(unittest.TestCase):
    def setUp(self):
        self.a = [8, 7, 2, 5, 3, 1]

    def test_n2(self):
        ans = arrays.find_pair_with_given_sum_n2(self.a, 11)
        expected_ans = (0, 4)
        self.assertEqual(ans, expected_ans)
        ans = arrays.find_pair_with_given_sum_n2(self.a, -10)
        expected_ans = (-1, -1)
        self.assertEqual(ans, expected_ans)

    def test_n_log_n(self):
        ans = arrays.find_pair_with_given_sum_n_logn(self.a, 11)
        expected_ans = (2, 5) # array is sorted thus indices are different
        self.assertEqual(ans, expected_ans)
        ans = arrays.find_pair_with_given_sum_n_logn(self.a, -10)
        expected_ans = (-1, -1)
        self.assertEqual(ans, expected_ans)

    def test_n(self):
        ans = arrays.find_pair_with_given_sum_n(self.a, 11)
        expected_ans = (0, 4)
        self.assertEqual(ans, expected_ans)
        ans = arrays.find_pair_with_given_sum_n(self.a, -10)
        expected_ans = (-1, -1)
        self.assertEqual(ans, expected_ans)


class TestCheckIfSubarrayWithSum0Exists(unittest.TestCase):
    def test_n(self):
        a = [-8, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4]
        expected_ans = True
        ans = arrays.check_if_subarray_with_sum_0_exists_n(a)
        self.assertEqual(ans, expected_ans)
        a = [-1, -2, -3, -4, -120]
        expected_ans = False
        ans = arrays.check_if_subarray_with_sum_0_exists_n(a)
        self.assertEqual(ans, expected_ans)


class TestReturnAllSubarraysWithSum0(unittest.TestCase):
    def test_n2(self):
        a = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
        expected_ans = [(0, 2), (0, 9), (1, 3), (2, 5), (3, 9), (5, 7)]
        ans = arrays.return_all_subarrays_with_sum_0_n2(a)
        self.assertEqual(ans, expected_ans)
        a = [2, 3, 4, 100]
        expected_ans = []
        ans = arrays.return_all_subarrays_with_sum_0_n2(a)
        self.assertEqual(ans, expected_ans)


class TestSortBinaryArray(unittest.TestCase):
    def test_n(self):
        a = [0, 1, 0, 0, 1, 0, 1, 1, 1, 0]
        expected_ans = sorted(a)
        ans = arrays.sort_binary_array_n(a)
        self.assertEqual(ans, expected_ans)
        a = [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1]
        expected_ans = sorted(a)
        ans = arrays.sort_binary_array_n(a)
        self.assertEqual(ans, expected_ans)
        a = [1, 0, 0, 0, 0, 0]
        expected_ans = sorted(a)
        ans = arrays.sort_binary_array_n(a)
        self.assertEqual(ans, expected_ans)


class TestFindDuplicateInLimitedRangeArray(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2, 3, 4, 5, 5, 6, 7]
        self.b = [1, 1, 2, 3, 4, 5]
        self.c = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
        self.expected_a = 5
        self.expected_b = 1
        self.expected_c = 6

    def test_find_duplicate_hashing_n_n(self):
        ans = arrays.find_duplicate_hashing_n_n(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_duplicate_hashing_n_n(self.b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_duplicate_hashing_n_n(self.c)
        self.assertEqual(ans, self.expected_c)

    def test_find_duplicate_make_negative_n_1(self):
        ans = arrays.find_duplicate_make_negative_n_1(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_duplicate_make_negative_n_1(self.b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_duplicate_make_negative_n_1(self.c)
        self.assertEqual(ans, self.expected_c)

    def test_find_duplicate_xor_n_1(self):
        ans = arrays.find_duplicate_xor_n_1(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_duplicate_xor_n_1(self.b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_duplicate_xor_n_1(self.c)
        self.assertEqual(ans, self.expected_c)

    def test_find_duplicate_sum_difference_n_1(self):
        ans = arrays.find_duplicate_sum_difference_n_1(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_duplicate_sum_difference_n_1(self.b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_duplicate_sum_difference_n_1(self.c)
        self.assertEqual(ans, self.expected_c)


class TestFindMaxLengthSubarrayOfGivenSum(unittest.TestCase):
    def setUp(self):
        self.a = [5, 6, -5, 5, 3, 5, 3, -2, 0]
        self.expected_a = [-5, 5, 3, 5]
        self.sum_a = 8

    def test_find_max_length_subarray_of_given_sum_n2(self):
        ans = arrays.find_max_length_subarray_of_given_sum_n2(self.a, self.sum_a)
        self.assertEqual(ans, self.expected_a)

    def test_find_max_length_subarray_of_given_sum_n(self):
        ans = arrays.find_max_length_subarray_of_given_sum_n(self.a, self.sum_a)
        self.assertEqual(ans, self.expected_a)
