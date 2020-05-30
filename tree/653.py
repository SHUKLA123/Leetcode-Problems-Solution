# Problem Id : 653 Problem Statement: Two Sum IV - Input is a BST



class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        array = self.inorderTraversal(root)
        if len(array) == 1:
            return False
        for i in array:
            if k-i in array and k-i != i:
                return True
        return False
        
    def inorderTraversal(self,root):
        if root == None:
            return []
        elements = []

        if root.left:
            elements += self.inorderTraversal(root.left)

        elements.append(root.val)

        if root.right:
            elements += self.inorderTraversal(root.right) 

        return elements