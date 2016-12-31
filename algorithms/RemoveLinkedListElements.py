# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        head, head.next = ListNode(0), head
        p = head
        
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        
        return head.next
        
