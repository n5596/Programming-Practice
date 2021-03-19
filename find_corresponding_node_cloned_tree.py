#https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q1 = [original]
        q2 = [cloned]
        while q1 != []:
            nq1 = []
            nq2 = []
            for i in range(len(q1)):
                n1 = q1[i]
                n2 = q2[i]
                if n1 == target:
                    return n2
                
                if n1.left != None:
                    nq1.append(n1.left)
                    nq2.append(n2.left)
                if n1.right != None:
                    nq1.append(n1.right)
                    nq2.append(n2.right)
            q1 = copy.copy(nq1)
            q2 = copy.copy(nq2)
        return
