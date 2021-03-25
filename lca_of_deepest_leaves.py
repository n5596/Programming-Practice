#https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root, curr_depth):
        if root == None:
            return 0, None, 0
        if root.left ==None and root.right == None: #leaf
            return curr_depth, root, 1
        a1, b1, f1 = self.find(root.left, curr_depth+1)
        a2, b2, f2 = self.find(root.right, curr_depth+1)
        
        if f1 == f2 and f1 == 1: #2 leaves
            print('leaf', a1, root.val)
            return a1, root, 0
        else:
            #print('other',root.val, a1,a2,b1.val,b2.val)
            if a1 > a2:
                return a1,b1,0
            elif a2 > a1:
                return a2,b2,0
            else:
                return a1, root, 0
        
        
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        ans1, ans2, ans3 = self.find(root, 0)
        #print(ans2.val)
        return ans2
