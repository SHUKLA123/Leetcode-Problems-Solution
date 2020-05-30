sentence = "hello from the other side"
searchWord = "they"
def test(sentence,searchWord):
	c = sentence.split(" ")
	for i in range(len(c)):
		if c[i].startswith(searchWord):
			return i+1
	return -1

print(test(sentence,searchWord))