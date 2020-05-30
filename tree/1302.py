# Problem Id : 1302, Problem Title : Deepest Leaves Sum
# Tags : Tree , DFS.(But I have tried Level order treversal)
# Level : Medium

#Given a binary tree, return the sum of values of its deepest leaves.

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# mene level order treversal use kiya tha,
# level order treversal karte samaye list me har level ki values ko store kari hai then sum kiya tha har list ko.
# return karva diya last vale ko 

def deepestLeavesSum(root):
    if root == None:
        return 0
    q = []
    l = []
    q.append(root)
    while q:
        temp = []
        s = []
        while q:
            
            a = q.pop(0)
            s.append(a.val)
            if a.left:
                temp.append(a.left)
            if a.right:
                temp.append(a.right)
        q = temp
        l.append(s)
    return sum(l[-1])