

leftover_list = []
def number_needed(a,b):
	a = str(a).lower()
	b = str(b).lower()
	for char in a:
		if char not in b:
			leftover_list.append(char)
	for char in b:
		if char not in a:
			leftover_list.append(char)
	print(len(leftover_list))

number_needed("abc","cde")
	