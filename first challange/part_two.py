import re
import time

time_start = time.time()

words_to_numbers = {
	'oneight':   18,
	'fiveight':  58,
	'threeight': 38,
	'nineight':  98,
	'twone':     21,
	'sevenine':  79,
	'eightwo':   82,
	'one':       1,
	'two':       2,
	'three':     3,
	'four':      4,
	'five':      5,
	'six':       6,
	'seven':     7,
	'eight':     8,
	'nine':      9,
}

with open("codes.txt", "r") as f:
	codes = f.readlines()


def concat_value(value):
	return int(str(value[0]) + str(value[-1]))


def splice_large_number(number):
	return [int(digit) for digit in str(number)]


def search_for_digits(string):
	pattern = '(' + '|'.join(words_to_numbers.keys()) + '|\\d+)'
	result = re.findall(pattern, string.lower())

	answer = []
	for string in result:
		if string.isdigit():
			if len(string) > 1:
				spliced_digits = splice_large_number(string)
				for digit in spliced_digits:
					answer.append(digit)
			else:
				answer.append(int(string))
		elif string in words_to_numbers:
			if len(str(words_to_numbers[string])) > 1:
				spliced_digits = splice_large_number(words_to_numbers[string])
				for digit in spliced_digits:
					answer.append(digit)
			else:
				answer.append(words_to_numbers[string])
	return answer


calibration_values = []
for code in codes:
	digits = search_for_digits(code)

	if digits:
		calibration_value = concat_value(digits)
		calibration_values.append(calibration_value)

total_sum = sum(calibration_values)
print(f"\ntotal_sum: {total_sum}")
print(f"took {time.time() - time_start} seconds")
