# Problem Id : 58 ,  Problem Title : Length of Last Word

# Easy

def lengthOfLastWord(s):
    if s== " "*len(s) or s == "":
        return 0
    s = s.split(" ")[::-1]
    for i in s:
        if i != "" or i!= " "*len(i):
            return len(i)