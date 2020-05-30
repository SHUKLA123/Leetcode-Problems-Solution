def repeatedSubstringPattern(self, s: str) -> bool:
    if len(s) == 1:
        return False
    x = s[0]
    i = 0
    while i != len(s):
        if s.count(x)*len(x) == len(s):
            return True
        i = i + 1
        x = s[:i]