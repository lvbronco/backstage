from typing import List, Tuple

def sum_of_nums(num: int) -> int:
	if num < 1 or num > 100:
		return 0
	return sum_of_list(list(range(1, num+1)))

def sum_of_list(num_list: List[int]) -> int:
	my_sum: int = 0
	for i in num_list:
		my_sum += i
	return my_sum

def create_list_of_sq(num: int) -> List[int]:
	if num < 1 or num > 100:
		return []
	return [x*x for x in range(1, num+1)]

def difference_value(num: int) -> int:
	sum_of_sq: int = sum_of_list(create_list_of_sq(num))
	sq_of_sum: int = sum_of_nums(num)**2
	return abs(sum_of_sq - sq_of_sum)

def order_values(tup: Tuple[int, int]):
	if tup[0] > tup[1]:
		return (tup[1], tup[0])
	return tup

def pythagorean_triples(a: int, b: int, c: int) -> bool:
	if a < 1 or b < 1 or c < 1:
		return False
	(a, c) = order_values((a, c))
	(b, c) = order_values((b, c))
	if c > 1000:
		return False
	return (a**2 + b**2) == c**2