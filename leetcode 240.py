# Problem id : 240. Problem title : Search a 2D Matrix II Difficulty : medium

#Write an efficient algorithm that searches for a value in an m x n matrix. 

#This matrix has the following properties:

# Solution : 2-d matrix is given we have to each row contain target or not if not in any row return False else return True. 

# 28 ms, faster than 96.57%

target = 20
matrix = [
			[1,4,7,11,15],
			[2,5,8,12,19],
			[3,6,9,16,22],
			[10,13,14,17,24],
			[18,21,23,26,30]
		 ]
def searchMatrix(matrix, target):
	for i in matrix:
		if target in sorted(i):
			return True
	return False
print(searchMatrix(matrix,target))