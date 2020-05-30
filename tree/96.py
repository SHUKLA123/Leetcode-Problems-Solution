# Problem Id : 96  Problem Statement : Unique Binary Search Trees

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

from math import factorial
def numTrees(n):
	if n <= 1 : 
	    return 1 

	# Catalan(n) is the sum of catalan(i)*catalan(n-i-1) 
	res = 0
	cn = factorial(2*n)
	nc = (factorial(n+1)*factorial(n))
	return cn//nc
print(numTrees(3))