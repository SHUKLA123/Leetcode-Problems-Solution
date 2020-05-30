# 409. Longest Palindrome 
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Runtime: 28 ms, faster than 83.64%
s = "abccccdd"
def longestPalindrome(s):
    a = Counter(s)
    count = 0
    counter = 0
    if len(a) == 1:
        return a[s[0]]
    for i,j in a.items():
        if j%2 == 0:
            count += j
        elif j%2 != 0 and j>2:
            count += (j-1)
            counter += 1 
        else:
            counter += 1
    return count+1 if counter>=1 else count
