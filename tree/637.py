# Problem Id : 637. Problem Title : Average of Levels in Binary Tree
# Tags : Tree 
# Level : Easy

# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

# Input: p = [1,2,3],  q =  [1,2,3]
# Output: True

# In this question, I applied the B.F.S.(level order treversal) and avarage every value 
# return every avg. value into the list (take all values of node of every level in seperated list) 
def averageOfLevels(self, root: TreeNode) -> List[float]:
    return self.level(root)

def level(self,root):
    q = []
    c = []
    q.append(root)
    while q:
        sums,count = 0, 0
        temp = []
        while q:
            n = q.pop(0)
            sums += n.val
            count += 1
            if n.left:
                temp.append(n.left)
            if n.right:
                temp.append(n.right)
        q = temp
        c.append(sums*1.0/count)
    return c

