def reverseBits(self, n):
    n = "{:032b}".format(n)
    return int(n[::-1],2)