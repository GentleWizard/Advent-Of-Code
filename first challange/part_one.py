import time

START = time.time()

with open("codes.txt", "r") as f:
	codes = f.readlines()

calibration_values = []
for code in codes:
	digits = [char for char in code if char.isdigit()]
	if digits:
		calibration_value = int(str(digits[0]) + str(digits[-1]))
		calibration_values.append(calibration_value)
	print(f"code: {code}")
	print(f"digits: {digits}")
	print(f"calibration_value: {calibration_value}")

total_sum = sum(calibration_values)
print(f"\ntotal_sum: {total_sum}")
print(f"took {time.time() - START} seconds")
