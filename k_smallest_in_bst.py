#https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, node, k):
        if root.left != None:
            a1, f1, node = self.inorder(root.left, node, k)

        if node == k:
            return root.val, 1, node+1
        node += 1

        if root.right != None:
            a2, f2, node = self.inorder(root.right, node, k)
        
        if root.left != None and f1 != 0:
            return a1, f1, node
        if root.right != None and f2 != 0:
            return a2, f2, node
        return 0,0,node
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans, flag,node = self.inorder(root, 1, k)
        return ans
