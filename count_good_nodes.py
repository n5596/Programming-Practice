#https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, root, maxk):
        if root == None:
            return 0
        if root.left == None and root.right == None: #leaf
            if root.val >= maxk:
                return 1
            return 0
    
        c1 = self.recurse(root.left, max(maxk, root.val))
        c2 = self.recurse(root.right, max(maxk, root.val))
        
        c3 = 0
        if root.val >= maxk:
            c3 = 1
        return c1+c2+c3
    
    def goodNodes(self, root: TreeNode) -> int:
        count = self.recurse(root, root.val)
        return count
