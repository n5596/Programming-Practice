#https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        if root == None:
            return []
        queue = [root]
        while queue != []:
            new_q = []
            mx = -math.inf
            for q in queue:
                if q.left != None:
                    new_q.append(q.left)
                if q.right != None:
                    new_q.append(q.right)
                if q.val > mx:
                    mx = q.val
            queue = new_q
            ans.append(mx)
        return ans
