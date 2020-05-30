def searchBST(root, val):
	# use recursion method for finding the search bst 
    def rec(root):
        if root:
            if root.val: return root
            elif root.right: return rec(root.right)
            return rec(root.left)
    
    return rec(root)