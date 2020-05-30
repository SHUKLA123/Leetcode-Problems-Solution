# Problem Id : 102. Problem Title : Binary Tree Level Order Traversal
# Tags : Tree , BFS
# Level : Medium

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Input: [3,9,20,null,null,15,7]
# Output: [
#   [3],
#   [9,20],
#   [15,7]
# ]

# In this question, I applied the B.F.S.(level order treversal) and store every level's node value in seperate lists and return that lists.

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None: 
        return

    q = []
    l = []
    q.append(root)
    while q:
        temp = []
        sum = []
        while q:
            
            a = q.pop(0)
            sum.append(a.val)
            if a.left:
                temp.append(a.left)
            if a.right:
                temp.append(a.right)
        q = temp
        l.append(sum)
    return l