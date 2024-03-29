import unittest
from parameterized import parameterized_class, parameterized
import arrays
from itertools import permutations


@parameterized_class(("array", "sum", "expected"), [
    ([8, 7, 2, 5, 3, 1], 11, (0, 4)),
    ([8, 7, 2, 5, 3, 1], -10, (-1, -1)),
    ([], 1, (-1, -1)),
    ([1], 1, (-1, -1)),
])
class TestFindPairWithGivenSum(unittest.TestCase):
    def test_n2(self):
        self.assertEqual(arrays.find_pair_with_given_sum_n2(self.array, self.sum), self.expected)

    def test_n(self):
        self.assertEqual(arrays.find_pair_with_given_sum_n(self.array, self.sum), self.expected)


@parameterized_class(("array", "sum", "expected"), [
    ([8, 7, 2, 5, 3, 1], 11, (2, 5)),
    ([8, 7, 2, 5, 3, 1], -10, (-1, -1)),
    ([], 1, (-1, -1)),
    ([1], 1, (-1, -1)),
])
class TestFindPairWithGivenSumNlogn(unittest.TestCase):
    def test_nlogn(self):
        self.assertEqual(arrays.find_pair_with_given_sum_nlogn(self.array, self.sum), self.expected)


class TestCheckIfSubarrayWithSum0Exists(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [-8, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4], True),
        ("test 2", [-1, -2, -3, -4, -120], False),
        ("test 3", [], False),
        ("test 4", [0], True),
        ("test 5", [1], False),
    ])
    def test_n(self, _, array, expected):
        self.assertEqual(arrays.check_if_subarray_with_sum_0_exists_n(array), expected)


class TestReturnAllSubarraysWithSum0(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [3, 4, -7, 3, 1, 3, 1, -4, -2, -2], [(0, 2), (0, 9), (1, 3), (2, 5), (3, 9), (5, 7)]),
        ("test 2", [2, 3, 4, 100], []),
        ("test 3", [], []),
        ("test 4", [0], [(0, 0)]),
        ("test 5", [1], []),
    ])
    def test_n2(self, _, array, expected):
        self.assertEqual(arrays.return_all_subarrays_with_sum_0_n2(array), expected)


class TestSortBinaryArray(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [0, 1, 0, 0, 1, 0, 1, 1, 1, 0]),
        ("test 2", [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1]),
        ("test 3", [1, 0, 0, 0, 0, 0]),
        ("test 3", []),
        ("test 4", [1]),
        ("test 5", [0]),
    ])
    def test_n(self, _, array):
        self.assertEqual(arrays.sort_binary_array_n(array), sorted(array))


@parameterized_class(("array", "expected"), [
    ([1, 2, 3, 4, 5, 5, 6, 7], 5),
    ([1, 1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10], 6),
])
class TestFindDuplicateInLimitedRangeArray(unittest.TestCase):
    def test_find_duplicate_hashing_n_n(self):
        self.assertEqual(self.expected, arrays.find_duplicate_hashing_n_n(self.array))

    def test_find_duplicate_make_negative_n_1(self):
        self.assertEqual(self.expected, arrays.find_duplicate_make_negative_n_1(self.array))

    def test_find_duplicate_xor_n_1(self):
        self.assertEqual(self.expected, arrays.find_duplicate_xor_n_1(self.array))

    def test_find_duplicate_sum_difference_n_1(self):
        self.assertEqual(self.expected, arrays.find_duplicate_sum_difference_n_1(self.array))


@parameterized_class(("array", "sum", "expected"), [
    ([5, 6, -5, 5, 3, 5, 3, -2, 0], 8, [-5, 5, 3, 5]),
    ([], 8, []),
    ([1, 2, 3, 4], 11, []),
    ([1], 1, [1]),
    ([1, 2, 3, 1, 1, 1], 3, [1, 1, 1]),
])
class TestFindMaxLengthSubarrayOfGivenSum(unittest.TestCase):
    def test_find_max_length_subarray_of_given_sum_n2(self):
        self.assertEqual(self.expected, arrays.find_max_length_subarray_of_given_sum_n2(self.array, self.sum))

    def test_find_max_length_subarray_of_given_sum_n(self):
        self.assertEqual(self.expected, arrays.find_max_length_subarray_of_given_sum_n(self.array, self.sum))


@parameterized_class(("array", "expected"), [
    ([-2, -10, 3, 1, 5, -11], 110),
    ([1, 2, 3, 4, 5, 6, 6, 7, 2], 42),
])
class TestFindMaximumProductOfTwoElementsInArray(unittest.TestCase):
    def test_find_maximum_product_of_two_elements_in_array_n2(self):
        self.assertEqual(self.expected, arrays.find_maximum_product_of_two_elements_in_array_n2(self.array))

    def test_find_maximum_product_of_two_elements_in_array_nlogn(self):
        self.assertEqual(self.expected, arrays.find_maximum_product_of_two_elements_in_array_nlogn(self.array))

    def test_find_maximum_product_of_two_elements_in_array_n(self):
        self.assertEqual(self.expected, arrays.find_maximum_product_of_two_elements_in_array_n(self.array))


@parameterized_class(("array", "expected"), [
    ([0, 1, 2, 1, 2, 0, 0, 2, 0, 2, 1, 2, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]),
    ([0, 1, 2], [0, 1, 2]),
    ([0, 1, 1, 1, 1, 1, 2], [0, 1, 1, 1, 1, 1, 2]),
    ([], []),
    ([1], [1]),
    ([0], [0]),
    ([0, 1], [0, 1]),
])
class TestDutchNationalFlagProblem(unittest.TestCase):
    def test_dutch_national_flag_problem_n(self):
        self.assertEqual(self.expected, arrays.dutch_national_flag_problem_n(self.array))


class TestMergeTwoSortedArraysInPlace(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [2, 4, 6, 7, 10, 20], [1, 2, 3, 4, 5], ([1, 2, 2, 3, 4, 4], [5, 6, 7, 10, 20])),
        ("test 2", [2, 4, 6, 7, 10, 20], [1], ([1, 2, 4, 6, 7, 10], [20]))
    ])
    def test_merge_two_sorted_arrays_in_place_mn(self, _, a, b, expected):
        self.assertEqual(expected, arrays.merge_two_sorted_arrays_in_place_mn(a, b))


class TestMergeTwoArraysOneContainingVacantZeros(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [0, 2, 3, 0, 6, 0, 0, 10, 12, 0], [1, 4, 8, 12, 13], [1, 2, 3, 4, 6, 8, 10, 12, 12, 13]),
    ])
    def test_merge_two_arrays_one_containing_vacant_zeros_mn(self, _, a, b, expected):
        self.assertEqual(expected, arrays.merge_two_arrays_one_containing_vacant_zeros_mn(a, b))


class TestIndexOfZeroToBeReplacedToGetMaxLengthSubarrayOfOnes(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], 13),
        ("test 2", [1, 1, 1, 1, 1, 1], -1),
        ("test 3", [0, 0, 0, 0, 0], 0),
        ("test 4", [0], 0),
        ("test 5", [], -1),
    ])
    def test_index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(self, _, array, expected):
        self.assertEqual(expected, arrays.index_of_zero_to_be_replaced_to_get_max_length_subarray_of_ones_n(array))


class TestFisherYatesShuffle(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ("test 2", [0, 1, 2, 3, 4]),
        ("test 3", [0, 1, 2]),
    ])
    def test_fisher_yates_shuffle_n(self, _, array):
        self.assertTrue(tuple(arrays.fisher_yates_shuffle_n(array.copy())) in list(permutations(array)))


class TestEverySecondElementGreaterThanItsNeighbours(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [9, 5, 3, 8, 2, 4, 7, 1, 0], [5, 9, 3, 8, 2, 7, 1, 4, 0]),
        ("test 2", [1], [1]),
        ("test 3", [], []),
    ])
    def test_every_second_element_greater_than_its_neighbours_n(self, _, array, expected):
        self.assertEqual(expected, arrays.every_second_element_greater_than_its_neighbours_n(array))


class TestFindEquilibriumIndexOfAnArray(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [0, -3, 5, -4, -2, 3, 1, 0], (0, 3, 7)),
        ("test 2", [0, 1, 2, 3, -10, 3, 4, -1], (4, 6)),
        ("test 3", [0, 1], ()),
        ("test 4", [1, 0, 1], (1, )),
        ("test 5", [], ()),
    ])
    def test_find_equilibrium_index_of_an_array_n(self, _, array, expected):
        self.assertEqual(expected, arrays.find_equilibrium_index_of_an_array_n(array))


class TestFindLongestConsecutiveSubarray(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [2, 4, 8, 12, 13, 14, 6, 9, 2, 7, 5], [4, 5, 6, 7, 8, 9]),
        ("test 2", [-1, -2, 0, 4, 12, 13, 14, 3, 1, 2], [-2, -1, 0, 1, 2, 3, 4]),
        ("test 3", [-1, 0, 1], [-1, 0, 1]),
        ("test 4", [-1], [-1]),
        ("test 5", [], []),
    ])
    def test_find_longest_consecutive_subarray_nlogn(self, _, array, expected):
        self.assertEqual(expected, arrays.find_longest_consecutive_subarray_nlogn(array))


class TestBoyerMooreMajorityAlgorithm(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [1, 2, 3, 2, 3, 0, -1], None),
        ("test 2", [1, 2, 3, 2, 3, 0, -1, 3, 3, 3, 1, 3, 3, 3], 3),
        ("test 3", [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7], None),
        ("test 4", [1, 2, 3, 4, 5, 7, 7, 7, 7, 7, 7, 7], 7),
        ("test 5", [1], 1),
        ("test 6", [], None),
    ])
    def test_boyer_moore_n_n(self, _, array, expected):
        self.assertEqual(expected, arrays.boyer_moore_n_n(array))


class TestMoveAllZerosToTheEnd(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [1, 0, 2, 0, 1, 0, 0, 0, 1], [1, 2, 1, 1, 0, 0, 0, 0, 0]),
        ("test 2", [0, 0, 0, 0], [0, 0, 0, 0]),
        ("test 3", [1, 2, 3, 4, 1], [1, 2, 3, 4, 1]),
        ("test 4", [0, 0, 0, 0, 1, 2, 3, 4], [1, 2, 3, 4, 0, 0, 0, 0]),
        ("test 5", [0], [0]),
        ("test 6", [], []),
    ])
    def test_move_all_zeros_to_the_end_n_1(self, _, array, expected):
        self.assertEqual(expected, arrays.move_all_zeros_to_the_end_n_1(array))


@parameterized_class(("array", "expected"), [
    ([1, 2, 3, 4, 5, 6], [720, 360, 240, 180, 144, 120]),
    ([-1, -10, 20, 4, 11], [-8800, -880, 440, 2200, 800]),
    ([0, 1, 2, 3, 4, 5], [120, 0, 0, 0, 0, 0]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([0], [1]),
    ([], []),
])
class TestReplaceEachElementWithProductOfEveryOtherElement(unittest.TestCase):
    def test_replace_each_element_with_product_of_every_other_element_n_n(self):
        self.assertEqual(self.expected, arrays.replace_each_element_with_product_of_every_other_element_n_n(self.array))

    def test_replace_each_element_with_product_of_every_other_element_n_1(self):
        self.assertEqual(self.expected, arrays.replace_each_element_with_product_of_every_other_element_n_1(self.array))


class TestLongestIncreasingSubsequence(unittest.TestCase):
    @parameterized.expand([
        ("test 1", [], []),
        ("test 2", [1, 2], [1, 2]),
        ("test 3", [1, 0, 2], [1, 2]),
        ("test 4", [3, 2, 1], []),
        ("test 5", [1, 2, 3, 0, 4, 5, 6, 0, 7, 8, -1, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    ])
    def test_longest_increasing_subsequence_nlogn(self, _, array, expected):
        self.assertEqual(expected, arrays.longest_increasing_subsequence_nlogn(array))
