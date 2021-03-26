#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        ans = []
        while queue != []:
            new_q = []
            n_val = []
            for q in queue:
                if q.left != None:
                    new_q.append(q.left)
                if q.right != None:
                    new_q.append(q.right)
                n_val.append(q.val)
            queue = new_q
            ans.append(n_val)
        return ans
