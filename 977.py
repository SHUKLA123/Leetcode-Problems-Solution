def sortedSquares(self, A: List[int]) -> List[int]:
    l = [i**2 for i in A]
    return sorted(l)
        