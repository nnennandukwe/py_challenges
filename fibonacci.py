
def fibonacci(n):

	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

nterms = 10

if nterms <= 0:
	print("Please enter a positive number.")
else:
	print("Fibonacci Sequence:")
	for i in range(nterms):
		print(fibonacci(i))