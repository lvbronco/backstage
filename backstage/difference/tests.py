from django.test import TestCase
import difference.utils.maths as maths

class MathsTest(TestCase):

	def test_sum_of_nums(self):
		test_sum_neg: int = maths.sum_of_nums(0)
		self.assertEqual(test_sum_neg, 0)

		test_sum_zero: int = maths.sum_of_nums(0)
		self.assertEqual(test_sum_zero, 0)

		test_sum_over_100: int = maths.sum_of_nums(101)
		self.assertEqual(test_sum_over_100, 0)

		test_sum_1: int = maths.sum_of_nums(1)
		self.assertEqual(test_sum_1, 1)

		test_sum_3: int = maths.sum_of_nums(3)
		self.assertEqual(test_sum_3, 6)


	def test_sum_of_list(self):
		test_sum: int = maths.sum_of_list([1,2,3])
		self.assertEqual(test_sum, 6)

		test_sum_sq: int = maths.sum_of_list([1,4,9])
		self.assertEqual(test_sum_sq, 14)

		test_sum_empty: int = maths.sum_of_list([])
		self.assertEqual(test_sum_empty, 0)

	def test_create_list_of_sq(self):
		test_list = maths.create_list_of_sq(3)
		self.assertEqual(test_list, [1, 4, 9])

		test_list_zero = maths.create_list_of_sq(0)
		self.assertEqual(test_list_zero, [])

		test_list_too_big = maths.create_list_of_sq(101)
		self.assertEqual(test_list_too_big, [])

	def test_difference_value(self):
		test_diff: int = maths.difference_value(10)
		self.assertEqual(test_diff, 2640)

		test_diff_1: int = maths.difference_value(1)
		self.assertEqual(test_diff_1, 0)

		test_diff_zero: int = maths.difference_value(0)
		self.assertEqual(test_diff_zero, 0)

	def test_order_values(self):
		test_tup = maths.order_values((0,1))
		self.assertEqual(test_tup, (0,1))

		test_tup = maths.order_values((1,0))
		self.assertEqual(test_tup, (0,1))

	def test_pythagorean_triples(self):
		test_abc = maths.pythagorean_triples(3,4,5)
		self.assertEqual(test_abc, True)

		test_abc = maths.pythagorean_triples(12,5,13)
		self.assertEqual(test_abc, True)

		test_abc = maths.pythagorean_triples(4,4,5)
		self.assertEqual(test_abc, False)