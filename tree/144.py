# Problem Id : 144. Problem Title : Binary Tree Preorder Traversal
# Tags : Tree , Stack (but for dfs we use the stack that's why we use stack here)
# Level : Medium

# Given a binary tree, return the preorder traversal of its nodes' values.

# Input: [1,null,2,3]
# Output: [1,2,3]

# see for bfs we use the queue dsa to store node value
# but for dfs we use the stack 
# I have applied pre-order (DFS) treversal.
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if root == None:
        return []
    element = []
    element.append(root.val)
    if root.left:
        element += self.preorderTraversal(root.left)
    if root.right:
        element += self.preorderTraversal(root.right)

    return element