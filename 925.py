def isLongPressedName(self, name: str, typed: str) -> bool:
    if name == typed:
        return True
    if name[0] != typed[0]:
        return False
    left = 0
    right = 0
    for i in name:
        flag = 0
        while right<len(typed):
            if typed[right] == i:
                flag = 1
                left = right
                right += 1
                break
            elif typed[right] != i and typed[left] != typed[right]:
                return False
            right = right + 1
        if flag  == 0:
            return False
    if right >= len(typed):
        return True
    else:
        for i in range(right,len(typed)):
            if typed[left] != typed[i]:
                return False
        return True