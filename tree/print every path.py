A, P = [], []
def dfs(N):
    if N == None: return
    P.append(N.val)
    if (N.left,N.right) == (None,None): A.append(''.join(map(str,P)))
    else: dfs(N.left), dfs(N.right)
    P.pop()
dfs(root)
print(A)