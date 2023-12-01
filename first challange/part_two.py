import re
import time

now = time.time()

with open("codes.txt", "r") as f:
	codes = f.readlines()


def search_for_digits(string, words):
	string = string.lower()
	words = [word.lower() for word in words]
	pattern = '(' + '|'.join(words) + '|\\d+)'
	result = re.findall(pattern, string)
	valid_digits = {
		'one':   1,
		'two':   2,
		'three': 3,
		'four':  4,
		'five':  5,
		'six':   6,
		'seven': 7,
		'eight': 8,
		'nine':  9,
		'zero':  0
	}
	answer = []
	for str in result:
		if str.isdigit():
			answer.append(int(str))
		elif str in valid_digits:
			answer.append(valid_digits[str])

	return answer


def split_large_numbers(digits):
	return [int(digit) for digit in str(digits)]


calibration_values = []
for code in codes:
	digits = search_for_digits(code, ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero'])
	i = 0
	while i < len(digits):
		number = digits[i]
		if number > 9:
			split_digits = split_large_numbers(number)
			digits = digits[:i] + split_digits + digits[i + 1:]
			i += len(split_digits)
		else:
			i += 1

	if digits:
		calibration_value = int(str(digits[0]) + str(digits[-1]))
		calibration_values.append(calibration_value)
	print(f"code: {code}")
	print(f"digits: {digits}")
	print(f"calibration_value: {calibration_value}")

total_sum = sum(calibration_values)
print(f"\ntotal_sum: {total_sum}")
print(f"Time: {time.time() - now}")
