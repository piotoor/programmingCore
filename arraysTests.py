import unittest
from csv import unix_dialect

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


class TestFindMaximumProductOfTwoElementsInArray(unittest.TestCase):
    def setUp(self):
        self.a = [-2, -10, 3, 1, 5, -11]
        self.expected_a = 110
        self.b = [1, 2, 3, 4, 5, 6, 6, 7, 2]
        self.expected_b = 42

    def test_find_maximum_product_of_two_elements_in_array_n2(self):
        ans = arrays.find_maximum_product_of_two_elements_in_array_n2(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_maximum_product_of_two_elements_in_array_n2(self.b)
        self.assertEqual(ans, self.expected_b)

    def test_find_maximum_product_of_two_elements_in_array_nlogn(self):
        ans = arrays.find_maximum_product_of_two_elements_in_array_nlogn(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_maximum_product_of_two_elements_in_array_nlogn(self.b)
        self.assertEqual(ans, self.expected_b)

    def test_find_maximum_product_of_two_elements_in_array_n(self):
        ans = arrays.find_maximum_product_of_two_elements_in_array_n(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_maximum_product_of_two_elements_in_array_n(self.b)
        self.assertEqual(ans, self.expected_b)


class TestDutchNationalFlagProblem(unittest.TestCase):
    def test_dutch_national_flag_problem_n(self):
        a = [0, 1, 2, 1, 2, 0, 0, 2, 0, 2, 1, 2, 0, 1]
        expected_a = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        ans = arrays.dutch_national_flag_problem_n(a)
        self.assertEqual(ans, expected_a)
        a = [0, 1, 2]
        expected_a = [0, 1, 2]
        ans = arrays.dutch_national_flag_problem_n(a)
        self.assertEqual(ans, expected_a)
        a = [0, 1, 1, 1, 1, 1, 2]
        expected_a = [0, 1, 1, 1, 1, 1, 2]
        ans = arrays.dutch_national_flag_problem_n(a)
        self.assertEqual(ans, expected_a)


class TestMergeTwoSortedArraysInPlace(unittest.TestCase):
    def test_merge_two_sorted_arrays_in_place_mn(self):
        a = [2, 4, 6, 7, 10, 20]
        b = [1, 2, 3, 4, 5]
        expected_a = [1, 2, 2, 3, 4, 4]
        expected_b = [5, 6, 7, 10, 20]
        ans_a, ans_b = arrays.merge_two_sorted_arrays_in_place_mn(a, b)
        self.assertEqual(ans_a, expected_a)
        self.assertEqual(ans_b, expected_b)


class TestMergeTwoArraysOneContainingVacantZeros(unittest.TestCase):
    def test_merge_two_arrays_one_containing_vacant_zeros_mn(self):
        a = [0, 2, 3, 0, 6, 0, 0, 10, 12, 0]
        b = [1, 4, 8, 12, 13]
        expected_a = [1, 2, 3, 4, 6, 8, 10, 12, 12, 13]
        ans = arrays.merge_two_arrays_one_containing_vacant_zeros_mn(a, b)
        self.assertEqual(ans, expected_a)


class TestIndexOfZeroToBeReplacedToGetMaxLengthSubarrayOfOnes(unittest.TestCase):
    def test_index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(self):
        a = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
        b = [1, 1, 1, 1, 1, 1]
        c = [0, 0, 0, 0, 0]
        expected_ans = 13
        expected_ans_b = -1
        expected_ans_c = -1
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(a)
        self.assertEqual(ans, expected_ans)
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(b)
        self.assertEqual(ans, expected_ans_b)
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(c)
        self.assertEqual(ans, expected_ans_c)


class TestFisherYatesShuffle(unittest.TestCase):
    def test_fisher_yates_shuffle_n(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ans = arrays.fisher_yates_shuffle_n(a.copy())
        self.assertNotEqual(a, ans)


class TestEverySecondElementGreaterThanItsNeighbours(unittest.TestCase):
    def test_every_second_element_greater_than_its_neighbours_n(self):
        a = [9, 5, 3, 8, 2, 4, 7, 1, 0]
        expected_a = [5, 9, 3, 8, 2, 7, 1, 4, 0]
        ans = arrays.every_second_element_greater_than_its_neighbours_n(a)
        self.assertEqual(ans, expected_a)


class TestFindEquilibriumIndexOfAnArray(unittest.TestCase):
    def test_find_equilibrium_index_of_an_array_n(self):
        a = [0, -3, 5, -4, -2, 3, 1, 0]
        expected_ans = (0, 3, 7)
        ans = arrays.find_equilibrium_index_of_an_array_n(a)
        self.assertEqual(ans, expected_ans)
        a = [0, 1, 2, 3, -10, 3, 4, -1]
        expected_ans = (4, 6)
        ans = arrays.find_equilibrium_index_of_an_array_n(a)
        self.assertEqual(ans, expected_ans)


class TestFindLongestConsecutiveSubarray(unittest.TestCase):
    def test_find_longest_consecutive_subarray_n_logn(self):
        a = [2, 4, 8, 12, 13, 14, 6, 9, 2, 7, 5]
        expected_ans = [4, 5, 6, 7, 8, 9]
        ans = arrays.find_longest_consecutive_subarray_n_logn(a)
        self.assertEqual(ans, expected_ans)
        a = [-1, -2, 0, 4, 12, 13, 14, 3, 1, 2]
        expected_ans = [-2, -1, 0, 1, 2, 3, 4]
        ans = arrays.find_longest_consecutive_subarray_n_logn(a)
        self.assertEqual(ans, expected_ans)