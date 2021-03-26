#https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = []
        even = []
        curr = copy.copy(head)
        c = 1
        while curr != None:
            if c % 2 == 0:
                even.append(curr.val)
            else:
                odd.append(curr.val)
            c += 1
            curr = curr.next
            
        curr = head
        i = 0
        while curr != None:
            if i < len(odd):
                curr.val = odd[i]
            else:
                j = i-len(odd)
                curr.val = even[j]
            curr = curr.next
            i += 1
        return head
