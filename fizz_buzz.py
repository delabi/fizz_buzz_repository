def fizz_buzz(n):
	num = n
	msg = ''
	if num % 3 == 0:
		msg += 'Fizz'
	if num % 5 == 0:
		msg += 'Buzz'
	return msg or num

# fizz_buzz(6)
# fizz_buzz(15)
