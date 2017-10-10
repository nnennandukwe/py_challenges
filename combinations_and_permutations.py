import math


# write out a readable function of the ordered comination function
# test your combination function using the variables from the problem
# for example, n = the 50 cats in total
# k = the 3 cats you are allowed to pick out of the 50 cats

# below is the FULL program of finding out all possible combinations and permutations of two numbers


def combination():
	
	# get input values from user and parse them to integers (whole numbers)
	n = int(input("How many cats at pet store? "))
	k = int(input("How many are you willing to take home? "))

	# put user input values n & k into the combination formula => n! / (n-k)! * k
	result = int(math.factorial(n) / (math.factorial(n - k) * math.factorial(k) ) )
	
	# print results
	print("There are %d different combinations of %d cats from the %d you can choose to take home!" % (result, n, k))

# un-comment the function combination() below in order to run the function in the console
combination()



def permutation():

	print("Welcome to the cat beauty contest!")

	# get input values from user and PARSE them to integers (whole numbers)
	n = int(input("How many cat contestants? "))
	k = int(input("How many winning places? "))

	# put user input values n & k into the permutation formula => n! / (n-k)!
	result = int(math.factorial(n) / (math.factorial(n-k)) )

	# print results
	print("There are %d number of ways that the contest can end." % (result))

# un-comment the function permutation() below in order to run the function in the console
permutation()


