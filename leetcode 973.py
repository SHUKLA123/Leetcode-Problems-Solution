# Problem Id : 973. Problem Title : K Closest Points to Origin

# type Medium

# Desciption : 
#We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique 
#(except for the order that it is in.)

# sol. find the squareroot(a**2+b**2) the add in dict sort the dict and return how K much to function .

from collections import Counter,OrderedDict
from operator import *
from math import sqrt
points = [[-5,4],[-6,-5],[4,6]]
K = 2
def kClosest(points, K):
        l = OrderedDict()
        answer = []
        for i in points:
            a = i[1]**2 + i[0] **2
            a = sqrt(a)
            l[tuple(i)] = a
        l = sorted(l.items(), key=lambda t: t[1])
        c = 1
        for i in l:
            if c == K:
                answer.append(list(i[0]))
                return answer
            answer.append(list(i[0]))
            c += 1 
print(kClosest(points,K))