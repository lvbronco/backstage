from typing import List

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