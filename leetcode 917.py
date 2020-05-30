# Problem Id : 917 Problem Title: Reverse Only Letters

# Easy



def reverseOnlyLetters(S):
    s = list(S)
    b = ""
    for i in range(len(s)):
        if s[i].isalpha():
            b = b  + s[i]
            s[i] = 0
    b = list(b[::-1])
    i = 0
    while b:
        if s[i] == 0:
            s[i] = b.pop(0)
        i = i + 1
    return "".join(s)