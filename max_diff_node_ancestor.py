#https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, root, maxv, minv, diff):
        if root == None:
            return 0
        if root.left == None and root.right == None: #leaf
            #print('leaf',root.val, maxv,minv, diff, abs(maxv-root.val), abs(minv-root.val), diff, max(abs(maxv-root.val), abs(minv-root.val), diff))
            return max(abs(maxv-root.val), abs(minv-root.val), diff, abs(maxv-minv))
        
        a1 =0
        a2 =0
        if root.left != None:
            a1 = self.recurse(root.left, max(maxv,root.val), min(minv, root.val), diff)
        if root.right != None:
            a2 = self.recurse(root.right, max(maxv,root.val), min(minv, root.val), diff)
        diff = max(abs(root.val-maxv), abs(root.val-minv))
        return max(a1, a2, diff)
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = self.recurse(root,root.val,root.val,0)
        return ans
        
