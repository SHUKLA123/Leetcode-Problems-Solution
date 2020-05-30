def isUnivalTree(self, root: TreeNode) -> bool:
    elements = self.inorder(root)
    prev = elements[0]
    for i in elements:
        if i != prev:
            return False
    return True
def inorder(self,root):
    if root == None:
        return []
    elements = []

    if root.left:
        elements += self.inorder(root.left)

    elements.append(root.val)

    if root.right:
        elements += self.inorder(root.right) 

    return elements