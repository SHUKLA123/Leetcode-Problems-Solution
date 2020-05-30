def increasingBST(self, root: TreeNode) -> TreeNode:
    array = self.inorderTraversal(root)
    print(array)
    root = cur = TreeNode(array[0])
    for i in range(1, len(array)):
        cur.right = TreeNode(array[i])
        cur = cur.right
    return root
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