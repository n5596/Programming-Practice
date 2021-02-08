# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        n1 = copy.copy(head)
        n2 = copy.copy(head)
        flag = 0
        while n1 != None and n2 != None and n2.next != None:
            if flag == 1 and n1 == n2: #cycle found
                flag = 2
                break
            n1 = n1.next
            n2 = n2.next.next
            flag = 1
            
        if flag == 2:
            return True
        return False
