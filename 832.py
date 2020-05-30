def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    c = []
    for i in A:
        d = []
        for j in i:
            if j == 0:
                d.append(1)
            elif j==1:
                d.append(0)
        c.append(d[::-1])
    return c