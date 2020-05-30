from heapq import heappush, heappop,nlargest,nsmallest,merge
from re import search,match,fullmatch,split,findall,finditer,sub,subn
from sys import *
from collections import Counter,OrderedDict
from operator import *
from math import e, pi, inf, nan, isinf, isnan, cos, acos, sin, asin, tan, atan, degrees, radians, log, log10, log2
from statistics import mean, median, variance, pvariance, pstdev
from random import random, randint, choice, shuffle
from itertools import product, combinations, combinations_with_replacement, permutations, accumulate,zip_longest
from queue import LifoQueue,Queue
#l = Queue(maxsize=4) l.put() l.get()
# itertools.accumulate(li1, operator.mul) ans [1,4,5,7] == [1,4,20,140]
# zip_longest( iterable1, iterable2, fillval) itertools.zip_longest('GesoGes', 'ekfrek', fillvalue ='_' )
#OrderedDict(sorted(d.items(), key=lambda t: t[0]))# dict sorted by key t[1] sorted by values
s = "tourist"
d = []
i = 0
for j in s:
	count = 0
	k = 0
	while k<=len(s):
		if i == len(s) or s[i] != j:
			break
		i = i + 1
		count += 1
		k = k + 1
	d.append(count)
print(max(d))