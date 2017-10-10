# gerund challenge

def gerund_infinitive(string):

	if string[-3:] == "ing":
		return "to " + string[:-3]
	else:
		return "That's not a gerund!"


print(gerund_infinitive("playing"))
