# Problem Id : 1022, Problem Title : Sum of Root To Leaf Binary Numbers

# Tags : Tree 

# Level : Easy

# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.

# Input: root = [1,0,1,0,1,0,1]
# Output: 22

# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22




def sumRootToLeaf(self, root: TreeNode) -> int:
    A, P = [], []
    def dfs(N):# mene traverse kiya har ek path ko or har ek path ko store kiya 
        if N == None: return
        P.append(N.val)
        if (N.left,N.right) == (None,None): A.append(''.join(map(str,P)))
        else: dfs(N.left), dfs(N.right)
        P.pop()
    dfs(root)
    count = 0
    for i in A:#then sare path ke last node ki value ko list me store kiya
        count += int("0b"+i,2)# then sabka bit count me add karta chalagaya and count me print kar diya.
    return count