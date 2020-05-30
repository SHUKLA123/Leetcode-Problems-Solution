def postorder(self, root: 'Node') -> List[int]:
    if root is None:
        return 
    res = []
    stack = [root]
    while stack:
        r = stack.pop()
        res.append(r.val)
        if r.children:
            for i in r.children:
                stack.append(i)
    return reversed(res)