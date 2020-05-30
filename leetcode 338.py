# Problem Id : 338  Problem Statement : Counting Bits Difficulty : Medium

#Given a non negative integer number num. 
#For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array

# Runtime is : 100ms
def test(a):
	l = []
	for i in range(a+1):
		bit = bin(i)
		l.append(bit.count("1"))
	return l
a = 2
print(test(a))