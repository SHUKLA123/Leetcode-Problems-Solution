def sortArrayByParity(self, A: List[int]) -> List[int]:
    left = 0
    right = 0
    while right<len(A):
        if A[right]%2 == 0:
            A[left],A[right] = A[right],A[left]
            left += 1
        right += 1
    return A