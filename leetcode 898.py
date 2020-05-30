# Problem Id 1304 Problem Statement : Find N Unique Integers Sum up to Zero # Easy

#Given an integer n, return any array containing n unique integers
# such that they add up to 0

#Runtime: 24 ms, faster than 97.04%  #Memory Usage: 13.9 MB, less than 100.00% 


def sumZero(n):
    l = []
    if n&1 is not 1:
        for i in range(1,n//2+1):
            l.append(i)
            l.append(-i)
    else:
        l.append(0)
        for i in range(1,n//2+1):
            l.append(i)
            l.append(-i)
    return l

n = 39

print(sumZero(n))