text = "To be or not to be"
def arrangeWords(text):
	text = text.split(" ")
	lst2 = sorted(text, key=len)
	lst2[0] = lst2[0].title()
	for i in range(1,len(lst2)):
		lst2[i] = lst2[i].lower() 
	return " ".join(lst2) 
print(arrangeWords(text))