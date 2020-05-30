def numJewelsInStones(self, j: str, s: str) -> int:
    l = list(j)
    count = 0
    for i in l:
        count += s.count(i)
    return count
    