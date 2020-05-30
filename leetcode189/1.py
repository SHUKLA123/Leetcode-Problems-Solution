startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5
def busyStudent(startTime, endTime, queryTime):
	count = 0
	for i,j in zip(startTime,endTime):
		if i<=queryTime and j>= queryTime:
			count += 1

	return count
print(busyStudent(startTime,endTime,queryTime))