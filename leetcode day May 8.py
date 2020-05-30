# Check If It Is a Straight Line (Leetcode)

# Question : You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# solution: Use Greedy approch as x2-x1/y2-y1 == x1-x/y1-y if it then continue else return False. Check for all points.


coordinates = [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
def checkstright(coordinates):
	n = len(coordinates)
	if len(coordinates) == 1:
		return True
	elif len(coordinates) == 2:
		x = coordinates[i][0]-coordinates[i-1][0]
		y = coordinates[i][1]-coordinates[i-1][1]
		x1 = coordinates[i-1][0]-coordinates[i-2][0]
		y1 = coordinates[i-1][1]-coordinates[i-2][1]
		a = x/y
		b = x1/y1
		if a == b:
			return True
		else:
			return False

	for i in range(2,n):
		x = coordinates[i][0]-coordinates[i-1][0]
		y = coordinates[i][1]-coordinates[i-1][1]
		x1 = coordinates[i-1][0]-coordinates[i-2][0]
		y1 = coordinates[i-1][1]-coordinates[i-2][1]
		if y != 0:
			a = x/y
		else:
			a = 0
		if y1 != 0:
			b = x1/y1
		else:
			b = 0
		if a != b:
			return False
	return True
print(checkstright(coordinates))