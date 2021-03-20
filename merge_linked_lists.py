#https://leetcode.com/problems/merge-in-between-linked-lists/
#Better solution possible

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        new_head = copy.copy(list1)
        t1 = copy.copy(list1)
        t2 = copy.copy(list2)
        curr = new_head
        flag = 0
        count = 0
        g = 0
        while t1 != None:
            if flag == 0 and count == a:
                flag = 1
                while t2 != None:
                    curr.next = copy.copy(t2)
                    curr = curr.next
                    t2 = t2.next
            if flag == 1 and count == b:
                flag = 2
                
            if flag != 1 and count != b:
                if g == 0 and curr == new_head:
                    g = 1
                else:
                    curr.next = copy.copy(t1)
                    curr = curr.next
            t1 = t1.next
            count += 1
        return new_head
