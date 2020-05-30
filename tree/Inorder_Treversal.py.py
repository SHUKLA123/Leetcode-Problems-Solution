# Probem Id : 94 Problem Statement : Binary Tree Inorder Traversal

# Description : Given a binary tree, return the inorder traversal of its nodes' values.

def inorderTraversal(root: TreeNode):
    if root == None:
        return []
    elements = []

    if root.left:
        elements += self.inorderTraversal(root.left)
    
    elements.append(root.val)
    
    if root.right:
        elements += self.inorderTraversal(root.right) 
    
    return elements