# reverse the string (medium)

s = "Niranjan is good"
def reverseWords(s):
	s = s.split(" ")
	p = []
	for i in s:
		if i == "":
			continue
		else:
			p.append(i)
	s = p
	s = " ".join(s[::-1])
	s = s.strip()
	return s
print(reverseWords(s))