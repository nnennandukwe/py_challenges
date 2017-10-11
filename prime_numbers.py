
def is_prime():

	#check if number is prime
	#if prime, true
	#if not prime, false
	print("Let's find out if your number is prime!")
	n = int(input("Give a positive integer: "))
	if n == 1:
		print("1 is not a prime number.")
		print(is_prime())
	elif n <= 0:
		print("0 and negative numbers are not positive integers.")
		print(is_prime())
	elif n == "":
		print("please provide a number.")
		print(is_prime())
	elif n % 2 == 0:
		print("True")
	else:
		print("False")

is_prime()