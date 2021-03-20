#https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, root, target):
        if root == None:
            return 0
        if root.left == None and root.right == None and root.val == target:
            return 1
        if root.left == None and root.right == None and root.val != target:
            return 0
        
        v1 = self.recurse(root.left, target)
        v2 = self.recurse(root.right, target)
        
        if v1 == 1:
            root.left = None
        if v2 == 1:
            root.right = None
        
        if root.left == None and root.right == None and root.val == target: #check again
            return 1
        return 0
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        ans = self.recurse(root, target)
        if ans == 1:
            return None
        return root
              
