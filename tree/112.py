# Problem Id : 112, Problem Title Path Sum
# Tags : Tree , DFS
# Level : Easy

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals the given sum.

# Input : root =  [5,4,8,11,null,13,4,7,2,null,null,null,1] , Sum = 22
# Output : True

# mene traverse kiya har ek path ko or har ek path ko store kiya ,
# then har sare path ko list me store kiya, har ek path ka sum() ki madat se sum nikala 
# then check kiya agar mila to True print kiya nahi to False
 

def hasPathSum(root, s):
    A, P = [], []
    def dfs(N):
        if N == None: return
        P.append(N.val)
        if (N.left,N.right) == (None,None): A.append(list(map(int,P)))
        else: dfs(N.left), dfs(N.right)
        P.pop()
    dfs(root)
    for i in A:
        if sum(i) == s:
            return True
    return False