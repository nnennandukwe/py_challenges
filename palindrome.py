

def palindrome(string):

	string = string.lower()
	return string[::-1] == string


print(palindrome("mom"))