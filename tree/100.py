# Problem Id : 100, Problem Title : Same Tree
# Tags : Tree , DFS
# Level : Easy

# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Input: p = [1,2,3],  q =  [1,2,3]
# Output: True

# this question proves your ability but its just a pop up question
# which means answer will pop up in your mind auto. 

def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if str(p) == str(q):
        return True
    else:
        return False
            