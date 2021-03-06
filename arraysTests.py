import unittest

import arrays


class TestFindPairWithGivenSum(unittest.TestCase):
    def setUp(self):
        self.a = [8, 7, 2, 5, 3, 1]
        self.b = []
        self.c = [1]
        self.expected_a = 0, 4
        self.expected_a2 = 2, 5
        self.expected_b = -1, -1

    def test_n2(self):
        ans = arrays.find_pair_with_given_sum_n2(self.a, 11)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_pair_with_given_sum_n2(self.a, -10)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_pair_with_given_sum_n2(self.b, 1)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_pair_with_given_sum_n2(self.c, 1)
        self.assertEqual(ans, self.expected_b)

    def test_nlogn(self):
        ans = arrays.find_pair_with_given_sum_nlogn(self.a, 11)
        self.assertEqual(ans, self.expected_a2)
        ans = arrays.find_pair_with_given_sum_nlogn(self.a, -10)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_pair_with_given_sum_nlogn(self.b, 1)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_pair_with_given_sum_nlogn(self.c, 1)
        self.assertEqual(ans, self.expected_b)

    def test_n(self):
        ans = arrays.find_pair_with_given_sum_n(self.a, 11)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_pair_with_given_sum_n(self.a, -10)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_pair_with_given_sum_n(self.b, 1)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_pair_with_given_sum_n(self.c, 1)
        self.assertEqual(ans, self.expected_b)


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
        a = []
        expected_ans = False
        ans = arrays.check_if_subarray_with_sum_0_exists_n(a)
        self.assertEqual(ans, expected_ans)
        a = [0]
        expected_ans = True
        ans = arrays.check_if_subarray_with_sum_0_exists_n(a)
        self.assertEqual(ans, expected_ans)
        a = [1]
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
        a = []
        expected_ans = []
        ans = arrays.return_all_subarrays_with_sum_0_n2(a)
        self.assertEqual(ans, expected_ans)
        a = [0]
        expected_ans = [(0, 0)]
        ans = arrays.return_all_subarrays_with_sum_0_n2(a)
        self.assertEqual(ans, expected_ans)
        a = [1]
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
        a = []
        expected_ans = sorted(a)
        ans = arrays.sort_binary_array_n(a)
        self.assertEqual(ans, expected_ans)
        a = [1]
        expected_ans = sorted(a)
        ans = arrays.sort_binary_array_n(a)
        self.assertEqual(ans, expected_ans)
        a = [0]
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
        self.b = []
        self.expected_b = []
        self.sum_b = 8
        self.c = [1, 2, 3, 4]
        self.expected_c = []
        self.sum_c = 11
        self.d = [1]
        self.expected_d = [1]
        self.sum_d = 1
        self.e = [1, 2, 3, 1, 1, 1]
        self.expected_e = [1, 1, 1]
        self.sum_e = 3

    def test_find_max_length_subarray_of_given_sum_n2(self):
        ans = arrays.find_max_length_subarray_of_given_sum_n2(self.a, self.sum_a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_max_length_subarray_of_given_sum_n2(self.b, self.sum_b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_max_length_subarray_of_given_sum_n2(self.c, self.sum_c)
        self.assertEqual(ans, self.expected_c)
        ans = arrays.find_max_length_subarray_of_given_sum_n2(self.d, self.sum_d)
        self.assertEqual(ans, self.expected_d)
        ans = arrays.find_max_length_subarray_of_given_sum_n2(self.e, self.sum_e)
        self.assertEqual(ans, self.expected_e)

    def test_find_max_length_subarray_of_given_sum_n(self):
        ans = arrays.find_max_length_subarray_of_given_sum_n(self.a, self.sum_a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.find_max_length_subarray_of_given_sum_n(self.b, self.sum_b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.find_max_length_subarray_of_given_sum_n(self.c, self.sum_c)
        self.assertEqual(ans, self.expected_c)
        ans = arrays.find_max_length_subarray_of_given_sum_n(self.d, self.sum_d)
        self.assertEqual(ans, self.expected_d)
        ans = arrays.find_max_length_subarray_of_given_sum_n(self.e, self.sum_e)
        self.assertEqual(ans, self.expected_e)


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
        a = []
        expected_a = []
        ans = arrays.dutch_national_flag_problem_n(a)
        self.assertEqual(ans, expected_a)
        a = [1]
        expected_a = [1]
        ans = arrays.dutch_national_flag_problem_n(a)
        self.assertEqual(ans, expected_a)
        a = [0]
        expected_a = [0]
        ans = arrays.dutch_national_flag_problem_n(a)
        self.assertEqual(ans, expected_a)
        a = [0, 1]
        expected_a = [0, 1]
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

        a = [2, 4, 6, 7, 10, 20]
        b = [1]
        expected_a = [1, 2, 4, 6, 7, 10]
        expected_b = [20]
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
        d = [0]
        e = []

        expected_ans = 13
        expected_ans_b = -1
        expected_ans_c = 0
        expected_ans_d = 0
        expected_ans_e = -1
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(a)
        self.assertEqual(ans, expected_ans)
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(b)
        self.assertEqual(ans, expected_ans_b)
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(c)
        self.assertEqual(ans, expected_ans_c)
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(d)
        self.assertEqual(ans, expected_ans_d)
        ans = arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(e)
        self.assertEqual(ans, expected_ans_e)


class TestFisherYatesShuffle(unittest.TestCase):
    def test_fisher_yates_shuffle_n(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ans = arrays.fisher_yates_shuffle_n(a.copy())
        self.assertNotEqual(a, ans)
        b = [0]
        ans = arrays.fisher_yates_shuffle_n(b.copy())
        self.assertEqual(b, ans)
        c = []
        ans = arrays.fisher_yates_shuffle_n(c.copy())
        self.assertEqual(c, ans)


class TestEverySecondElementGreaterThanItsNeighbours(unittest.TestCase):
    def test_every_second_element_greater_than_its_neighbours_n(self):
        a = [9, 5, 3, 8, 2, 4, 7, 1, 0]
        expected_a = [5, 9, 3, 8, 2, 7, 1, 4, 0]
        ans = arrays.every_second_element_greater_than_its_neighbours_n(a)
        self.assertEqual(ans, expected_a)
        a = [1]
        expected_a = [1]
        ans = arrays.every_second_element_greater_than_its_neighbours_n(a)
        self.assertEqual(ans, expected_a)
        a = []
        expected_a = []
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
        a = [0, 1]
        expected_ans = ()
        ans = arrays.find_equilibrium_index_of_an_array_n(a)
        self.assertEqual(ans, expected_ans)
        a = [1, 0, 1]
        expected_ans = (1,)
        ans = arrays.find_equilibrium_index_of_an_array_n(a)
        self.assertEqual(ans, expected_ans)
        a = []
        expected_ans = ()
        ans = arrays.find_equilibrium_index_of_an_array_n(a)
        self.assertEqual(ans, expected_ans)


class TestFindLongestConsecutiveSubarray(unittest.TestCase):
    def test_find_longest_consecutive_subarray_nlogn(self):
        a = [2, 4, 8, 12, 13, 14, 6, 9, 2, 7, 5]
        expected_ans = [4, 5, 6, 7, 8, 9]
        ans = arrays.find_longest_consecutive_subarray_nlogn(a)
        self.assertEqual(ans, expected_ans)
        a = [-1, -2, 0, 4, 12, 13, 14, 3, 1, 2]
        expected_ans = [-2, -1, 0, 1, 2, 3, 4]
        ans = arrays.find_longest_consecutive_subarray_nlogn(a)
        self.assertEqual(ans, expected_ans)
        a = [-1, 0, 1]
        expected_ans = [-1, 0, 1]
        ans = arrays.find_longest_consecutive_subarray_nlogn(a)
        self.assertEqual(ans, expected_ans)
        a = [-1]
        expected_ans = [-1]
        ans = arrays.find_longest_consecutive_subarray_nlogn(a)
        self.assertEqual(ans, expected_ans)
        a = []
        expected_ans = []
        ans = arrays.find_longest_consecutive_subarray_nlogn(a)
        self.assertEqual(ans, expected_ans)


class TestBoyerMooreMajorityAlgorithm(unittest.TestCase):
    def test_boyer_moore_n_n(self):
        self.a = [1, 2, 3, 2, 3, 0, -1]
        self.expected_a = None
        self.b = [1, 2, 3, 2, 3, 0, -1, 3, 3, 3, 1, 3, 3, 3]
        self.expected_b = 3
        self.c = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7]
        self.expected_c = None
        self.d = [1, 2, 3, 4, 5, 7, 7, 7, 7, 7, 7, 7]
        self.expected_d = 7
        self.e = [1]
        self.expected_e = 1
        self.f = []
        self.expected_f = None
        ans_a = arrays.boyer_moore_n_n(self.a)
        self.assertEqual(ans_a, self.expected_a)
        ans_b = arrays.boyer_moore_n_n(self.b)
        self.assertEqual(ans_b, self.expected_b)
        ans_c = arrays.boyer_moore_n_n(self.c)
        self.assertEqual(ans_c, self.expected_c)
        ans_d = arrays.boyer_moore_n_n(self.d)
        self.assertEqual(ans_d, self.expected_d)
        ans_e = arrays.boyer_moore_n_n(self.e)
        self.assertEqual(ans_e, self.expected_e)
        ans_f = arrays.boyer_moore_n_n(self.f)
        self.assertEqual(ans_f, self.expected_f)


class TestMoveAllZerosToTheEnd(unittest.TestCase):
    def test_move_all_zeros_to_the_end_n_1(self):
        a = [1, 0, 2, 0, 1, 0, 0, 0, 1]
        expected_a = [1, 2, 1, 1, 0, 0, 0, 0, 0]
        b = [0, 0, 0, 0]
        expected_b = [0, 0, 0, 0]
        c = [1, 2, 3, 4, 1]
        expected_c = [1, 2, 3, 4, 1]
        d = [0, 0, 0, 0, 1, 2, 3, 4]
        expected_d = [1, 2, 3, 4, 0, 0, 0, 0]
        e = [0]
        expected_e = [0]
        f = []
        expected_f = []
        ans_a = arrays.move_all_zeros_to_the_end_n_1(a)
        self.assertEqual(ans_a, expected_a)
        ans_b = arrays.move_all_zeros_to_the_end_n_1(b)
        self.assertEqual(ans_b, expected_b)
        ans_c = arrays.move_all_zeros_to_the_end_n_1(c)
        self.assertEqual(ans_c, expected_c)
        ans_d = arrays.move_all_zeros_to_the_end_n_1(d)
        self.assertEqual(ans_d, expected_d)
        ans_e = arrays.move_all_zeros_to_the_end_n_1(e)
        self.assertEqual(ans_e, expected_e)
        ans_f = arrays.move_all_zeros_to_the_end_n_1(f)
        self.assertEqual(ans_f, expected_f)


class TestReplaceEachElementWithProductOfEveryOtherElement(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2, 3, 4, 5, 6]
        self.expected_a = [720, 360, 240, 180, 144, 120]
        self.b = [-1, -10, 20, 4, 11]
        self.expected_b = [-8800, -880, 440, 2200, 800]
        self.c = [0, 1, 2, 3, 4, 5]
        self.expected_c = [120, 0, 0, 0, 0, 0]
        self.d = [1, 2]
        self.expected_d = [2, 1]
        self.e = [1]
        self.expected_e = [1]
        self.f = [0]
        self.expected_f = [1]
        self.g = []
        self.expected_g = []

    def test_replace_each_element_with_product_of_every_other_element_n_n(self):
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_n(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_n(self.b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_n(self.c)
        self.assertEqual(ans, self.expected_c)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_n(self.d)
        self.assertEqual(ans, self.expected_d)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_n(self.e)
        self.assertEqual(ans, self.expected_e)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_n(self.f)
        self.assertEqual(ans, self.expected_f)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_n(self.g)
        self.assertEqual(ans, self.expected_g)

    def test_replace_each_element_with_product_of_every_other_element_n_1(self):
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_1(self.a)
        self.assertEqual(ans, self.expected_a)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_1(self.b)
        self.assertEqual(ans, self.expected_b)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_1(self.c)
        self.assertEqual(ans, self.expected_c)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_1(self.d)
        self.assertEqual(ans, self.expected_d)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_1(self.e)
        self.assertEqual(ans, self.expected_e)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_1(self.f)
        self.assertEqual(ans, self.expected_f)
        ans = arrays.replace_each_element_with_product_of_every_other_element_n_1(self.g)
        self.assertEqual(ans, self.expected_g)


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence_nlogn(self):
        a = []
        expected = []
        ans = arrays.longest_increasing_subsequence_nlogn(a)
        self.assertEqual(ans, expected)
        a = []
        expected = []
        ans = arrays.longest_increasing_subsequence_nlogn(a)
        self.assertEqual(ans, expected)
        a = [1, 2]
        expected = [1, 2]
        ans = arrays.longest_increasing_subsequence_nlogn(a)
        self.assertEqual(ans, expected)
        a = [1, 0, 2]
        expected = [1, 2]
        ans = arrays.longest_increasing_subsequence_nlogn(a)
        self.assertEqual(ans, expected)
        a = [3, 2, 1]
        expected = []
        ans = arrays.longest_increasing_subsequence_nlogn(a)
        self.assertEqual(ans, expected)
        a = [1, 2, 3, 0, 4, 5, 6, 0, 7, 8, -1, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = arrays.longest_increasing_subsequence_nlogn(a)
        self.assertEqual(ans, expected)
