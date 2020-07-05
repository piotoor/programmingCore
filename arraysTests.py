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
