target = [1,3]
n = 4
# ["Push","Push","Pop","Push"]
def buildArray(target, n):
	l = []
	i = 1
	while i<=sorted(target)[-1]:
		if i in target:
			l.append("Push")
		else:
			l.append("Push")
			l.append("Pop")
		i =  i + 1
	# for i in range(n):
	# 	print(i+1)
	# 	print(i+1,target[i])
	# 	if i+1 == target[i]:
	# 		l.append("push")
	# 	else:
	# 		l.append("push")
	# 		l.append("pop")
	return l
print(buildArray(target,n))