

def anagram(string_one, string_two):

	string_one = string_one.lower()
	string_two = string_two.lower()

	return sorted(string_one) == sorted(string_two)

print(anagram("balloon", "iceman"))
