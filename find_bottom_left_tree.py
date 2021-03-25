#https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue != []:
            new_q = []
            for q in queue:
                if q.left != None:
                    new_q.append(q.left)
                if q.right != None:
                    new_q.append(q.right)
            if new_q == []: #last row
                return queue[0].val
            queue = new_q
        return queue[0].val
