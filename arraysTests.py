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
        expected_ans = (0, 4)
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