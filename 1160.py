def countCharacters(self, words: List[str], chars: str) -> int:
    a = Counter(chars)
    count = 0
    for i in words:
        b = Counter(i)
        flag = 0
        for j,k in b.items():
            if b[j]>a[j]:
                flag = 1
                break
            if j not in a.keys():
                flag = 1
                break
        if flag == 0:
            count += len(i)
        
    return count