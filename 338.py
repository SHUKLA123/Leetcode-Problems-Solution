def countBits(self, num: int) -> List[int]:
    l = []
    for i in range(num+1):
        bit = bin(i)
        l.append(bit.count("1"))
    return l