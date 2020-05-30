# Problem Id :  230. Problem Statement : Kth Smallest Element in a BST

# Details :
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.


def kthSmallest(root, k):
     def inorderTraversal(root: TreeNode):
        if root == None:
            return []
        elements = []

        if root.left:
            elements += inorderTraversal(root.left)

        elements.append(root.val)

        if root.right:
            elements += inorderTraversal(root.right) 

        return elements
     return inorderTraversal(root)[k-1]

root = [3,1,4,null,2]
k = 1
print(kthSmallest(root,k))