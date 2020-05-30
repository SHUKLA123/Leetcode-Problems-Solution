def rotateString(self, A: str, B: str) -> bool:
    i = 0
    if A == B:
        return True
    while i != len(A):
        A = A[1:]+A[0]
        if A == B:
            return True
        i += 1
    return False