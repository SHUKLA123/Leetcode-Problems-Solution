def findLongestWord(self, s: str, d: List[str]) -> str:
    l = []
    for i in d:
        left =0
        right = 0
        while right<=len(s):
            if left == len(i):
                l.append(i)
                break
            if right == len(s):
                break
            if i[left] == s[right]:
                left= left + 1
                right = right + 1
            elif i[left] != s[right]:
                right = right + 1
    l = sorted(l)
    return max(l, key = len) if l else "" 