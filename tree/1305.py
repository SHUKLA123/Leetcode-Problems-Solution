# Problem Id : 1305. Problem Title  : All Elements in Two Binary Search Trees
# Tags : Tree, Sort
# Level : Medium

# Given two binary search trees root1 and root2.
# Return a list containing all the integers from both trees sorted in ascending order.


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# You have two method :
# simply apply inorder treversal for both root and add the both list and print the sorted(list)
# or which i have used : find all path, add into list, sorted karke print karva do


def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    A, P = [], []
    def dfs(N):
        if N == None: return
        P.append(N.val)
        if (N.left,N.right) == (None,None): A.append(list(map(int,P)))
        else: dfs(N.left), dfs(N.right)
        P.pop()
    dfs(root1)
    c = A
    A = []
    dfs(root2)
    l=[]
    for i in sorted(c):
        for j in i:
            l.append(j)
    l1 = []
    for i in sorted(A):
        for j in i:
            l1.append(j)
    return sorted(list(list(set(l))+list(set(l1))))