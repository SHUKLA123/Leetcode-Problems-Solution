# Problem Id : 434 Problem Statement : Number of Segments in a String
# Diff : Easy
#Description : 
# Count the number of segments in a string,
# where a segment is defined to be a contiguous sequence of non-space characters.

# Please note that the string does not contain any non-printable characters.

def countSegments(s):
    if s ==  "" or s.strip() == "":
        return 0
    s = s.strip()
    s = s.split(" ")
    count = 0
    for i in s:
        a = len(i)
        if i != " "*a:
            count += 1
    return count