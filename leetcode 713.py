def closestNumber(a, b, x):
	if b == 1:
		count = a
		count1 = a
		c = a
	else:
		count = pow(a,b)
		count1 = count
		c = count1

	if b <0 and a != 1:
		return 0
	elif b<0 and a == 1 or x == 1:
		return 1
	while True:
		if count%x == 0:
			break
		count = count - 1
	while True:
		if count1%x == 0:
			break
		count1 = count1 + 1
	a = [(c-count,count),(count1-c,count1)]
	return min(a)[1]



a,b,x = 184804527,1, 38664371
# a,b,x = 749242874, 0, 424268981
# a,b,x = 782, -3, 135497282
# a,b,x = 827338328, 0, 84420926
# a,b,x = 295, -1, 632621730
# a,b,x = 84354896, 0, 433925858
# a,b,x = 538, -2, 548233368
# a,b,x = 86, 4, 760313751
# a,b,x = 889949179 ,0 ,356426809
# a,b,x = 820, 2, 918502652
# a,b,x = 717, -1, 264095061
# a,b,x = 750, 2, 984210013
# a,b,x = 859 ,-0, 956297540
# a,b,x = 975962379 ,0, 463480571
# a,b,x = 927613903 ,1, 892066602
# a,b,x = 660261757 ,0, 603570493
# a,b,x = 593210442 ,0, 485560281
# a,b,x = 947348620 ,0, 894429690

print(closestNumber(a,b,x))