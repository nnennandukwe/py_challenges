
def change_string(string):
	# turn 3 2 1 into 123:
	# from 321 to 321
	# from 321 to 123

	#get rid of whitespace
	#return reverse string
	collapsed = string.replace(' ','')
	reverse = collapsed[::-1]
	print(reverse)

change_string("5 4 3 2 1")

