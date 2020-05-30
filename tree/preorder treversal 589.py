def preorder(root):
    if root == []:
        return 
    res = []
    stack = [root]
    while stack:
        r = stack.pop()
        res.append(r.val)
        if r.children:
            for i in reversed(r.children):
                stack.append(i)
    return res