# Problem Id : 104, Problem Title : Maximum Depth of Binary Tree
# Tags : Tree , DFS
# Level : Easy

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

def maxDepth(root):
    if root == None:
        return 0
    A, P = [], []
    def dfs(N):# mene traverse kiya har ek path ko or har ek path ko store kiya 
        if N == None: return
        P.append(N.val)
        if (N.left,N.right) == (None,None): 
            A.append('$'.join(map(str,P)))
        else: dfs(N.left), dfs(N.right)
        P.pop()
    dfs(root)
    # In A at line : 15, then sare path ke last node ki value ko list me store kiya
    return sorted(A,key = len)[-1].count("$")+1 #then print kara diya lagest value ko