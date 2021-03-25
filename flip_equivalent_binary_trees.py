#https://leetcode.com/problems/flip-equivalent-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        q1 = [root1]
        q2 = [root2]
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        
        if root1.val != root2.val:
            return False

        
        while q1 != [] and q2 != []:
            new_q1 = []
            new_q2 = []
            if len(q1) != len(q2):
                return False
            
            for i in range(len(q1)):
                qa = q1[i]
                qb = q2[i]
                
                if qa.left == None and qb.left == None and qa.right == None and qb.right == None: #leaf
                    continue
                    
                #one branch None for both
                if qa.left == None and qb.left == None and qa.right != None and qb.right != None:    
                    if qa.right.val == qb.right.val:
                        new_q1.append(qa.right)
                        new_q2.append(qb.right)
                        continue
                    else:
                        return False
                if qa.right == None and qb.right == None and qa.left != None and qb.left != None:
                    if qa.left.val == qb.left.val:
                        new_q1.append(qa.left)
                        new_q2.append(qb.left)
                        continue
                    else:
                        return False
                    
                if qa.left == None and qb.right == None and qa.right != None and qb.left != None:
                    if qa.right.val == qb.left.val:
                        new_q1.append(qa.right)
                        new_q2.append(qb.left)
                        continue
                    else:
                        return False
                    
                if qa.right == None and qb.left == None and qa.left != None and qb.right != None:
                    if qa.left.val == qb.right.val:
                        new_q1.append(qa.left)
                        new_q2.append(qb.right)
                        continue
                    else:
                        return False
                
                #one branch None for one
                if qa.left == None or qb.left == None or qa.right == None or qb.right == None:
                    return False

                if qa.left.val == qb.left.val and qa.right.val == qb.right.val:
                    if qa.left != None:
                        new_q1.append(qa.left)
                        new_q2.append(qb.left)
                    if qa.right != None:
                        new_q1.append(qa.right)
                        new_q2.append(qb.right)
                elif qa.right.val == qb.left.val and qa.left.val == qb.right.val:
                    if qa.right != None:
                        new_q1.append(qa.right)
                        new_q2.append(qb.left)         
                    if qa.left != None:
                        new_q1.append(qa.left)
                        new_q2.append(qb.right)
                else:
                    return False
            q1 = copy.copy(new_q1)
            q2 = copy.copy(new_q2)
        return True
