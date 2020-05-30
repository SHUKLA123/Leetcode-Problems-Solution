def hammingWeight(self, n: int) -> int:
    return str('{:032b}'.format(n)).count("1")