def test2(num):
    A = list(str(num))
    ans = A[:]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            A[i], A[j] = A[j], A[i]
            if A > ans: ans = A[:]
            A[i], A[j] = A[j], A[i]

    return int("".join(ans))


def test(num):
	list_n = list(str(num))
	max = list_n[:]
	for i in range(len(list_n)):
		for j in range(i+1,len(list_n)):
			list_n[i],list_n[j] = list_n[j],list_n[i]
			if max<list_n:
				max = list_n[:]
			list_n[i], list_n[j] = list_n[j], list_n[i]
	return max


#num = 2736
#num = 4521
#num = 7166
#num = 4516
num = 1993
print(test2(num))
print(test(num))