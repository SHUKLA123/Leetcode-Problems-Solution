def checkIfExist(self, arr: List[int]) -> bool:
    if arr[:] == [0]*len(arr):
        return True
    for i in arr:
        if i == 0:
            continue
        if i/2 in arr:
            print(i/2)
            return True
    return False