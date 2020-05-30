def test(source):
	l = []
	flag = 0
	for i in source:
		if not i.startswith("/*") and not i.endswith("*/") and flag == 0 and "//" not in i :
			l.append(i)
		elif "//" in i:
			l.append("  ") 
		elif i.startswith("/*") and not i.endswith("*/"):
			flag = 1
		elif not i.startswith("/*") and i.endswith("*/"):
			flag = 0

	return l

source = ["a/*comment", "line", "more_comment*/b"]
print(test(source))
#["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]