# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
            
        t = head.next
        prev = head
        
        while t is not None:
            if t.val == prev.val:
                prev.next = t.next
                t = prev
                
            prev = t
            t = t.next
        
        return head
            
            
