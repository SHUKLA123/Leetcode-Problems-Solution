# Problem Id : 872, Problem Title : Leaf-Similar Trees
# Tags : Tree , DFS
# Level : Easy

#Given a binary tree, return the sum of values of its deepest leaves.

# Input: root = [3,5,1,6,2,9,8,null,null,7,4]
# Output: True


def leafSimilar(root1, root2):
    A, P = [], []
    def dfs(N): # mene traverse kiya har ek path ko or har ek path ko store kiya 
        if N == None: return
        P.append(N.val)
        if (N.left,N.right) == (None,None):
            A.append(P[-1])
        else: dfs(N.left), dfs(N.right)
        P.pop()
    dfs(root1)
    c = A #then sare path ke last node ki value ko list me store kiya
    A = [] 
    dfs(root2)# same procedure for second tree (root 2) 
    if c == A:# then check kiya agar dono ki list same hai to True else False
        return True
    else:
        return False


