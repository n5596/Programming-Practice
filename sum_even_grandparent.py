#https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        count = 0
        queue = [root]
        while queue != []:
            new_queue = []
            for q in queue:
                if q.left != None:
                    new_queue.append(q.left)
                if q.right != None:
                    new_queue.append(q.right)
                if q.val % 2 == 0:
                    a1 = q.left
                    a2 = q.right
                    if a1 != None:
                        if a1.left != None:
                            count += a1.left.val
                        if a1.right != None:
                            count += a1.right.val
                    if a2 != None:
                        if a2.left != None:
                            count += a2.left.val
                        if a2.right != None:
                            count += a2.right.val
                queue = copy.copy(new_queue)
        return count
