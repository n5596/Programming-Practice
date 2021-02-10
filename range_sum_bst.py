#https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: TreeNode, low: int, high: int) -> int:
        num = 0
        if low <= root.val and root.left != None:
            #print('travel left')
            num += self.traverse(root.left, low, high)
        if root.val <= high and root.right != None:
            #print('travel right')
            num += self.traverse(root.right, low, high)
        
        answer = 0
        if root.val <= high and low <= root.val:
            answer = root.val
        return num + answer
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        answer = self.traverse(root, low, high)
        return answer
