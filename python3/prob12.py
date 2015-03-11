def count_digits(n):
	count = 0
	while n > 0:
		count = count + 1
		n = n / 10
	return count
print count_digits(1010)
print count_digits(11)