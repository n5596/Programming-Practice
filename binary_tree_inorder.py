#https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, root, values):
        if root == None:
            return values
        if root.left == None and root.right == None: #leaf
            values.append(root.val)
            return values
        
        v1 = self.recurse(root.left, values)
        v1.append(root.val)
        v2 = self.recurse(root.right, v1)
        return v2
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = self.recurse(root, [])
        return ans
