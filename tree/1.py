# Jab Koi treversal defined nahi kari ho to inorder treversal hi main mani jati hai
# inoder me self._inorder(p.left,l) l.append() se phele aayega 
# preorder me self._preorder me l.append() ke baad ye self._preorder(p.left,l) ayega
# postorder me self._postorder me l.append() sabse niche aayega

# Problem id : 938 Problem Statement : Range Sum of BST ,Difficulty

# Desc : Given the root node of a binary search tree, 
# return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

#  288 ms, faster than 37.09% 

def rangeSumBST(self, root, L, R):
        l = []
        self._inorder(root,l)
        a = l.index(L)
        b = l.index(R)
        count = 0
        for i in range(a,b+1):
            count += l[i]
        return count
    def _inorder(self,p,l):
        if p is None:
            return
        self._inorder(p.left,l)
        l.append(p.val)
        self._inorder(p.right,l)

  #   def _preorder(self,p,l):
  #       if p is None:
  #           return
  #       l.append(p.val)
		# self._preorder(p.left,l)
  #       self._preorder(p.right,l)


  #   def _postorder(self,p,l):
  #       if p is None:
  #           return
  #       self._postorder(p.left,l)
  #       self._postorder(p.right,l)
  #       l.append(p.val)