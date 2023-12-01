with open("codes.txt", "r") as f:
	codes = f.readlines()

calibration_values = []
for code in codes:
	digits = [char for char in code if char.isdigit()]
	if digits:
		calibration_value = int(str(digits[0]) + str(digits[-1]))
		calibration_values.append(calibration_value)

total_sum = sum(calibration_values)
print(total_sum)
