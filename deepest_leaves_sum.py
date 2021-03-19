#https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        ans = 0
        while queue != []:
            ans = 0
            new_queue = []
            for q in queue:
                if q.left != None:
                    new_queue.append(q.left)
                if q.right != None:
                    new_queue.append(q.right)
                ans += q.val
            print(ans)
            queue = copy.copy(new_queue)
        return ans
