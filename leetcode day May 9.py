# Valid Perfect Square

# Question : Given a positive integer num, write a function which returns True if num is a perfect square else False.

# solution : see
from math import sqrt
num = 14
def squr(num):
	x = sqrt(num)
	if x == int(x):
		return True
	else:
		return False
print(squr(num))