def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    x = len(arr)
    i = 0
    while i<len(arr):
        if arr[i] == 0:
            arr.insert(i,0)
            i = i + 1
        i = i + 1
    while len(arr) != x:
        arr.pop()