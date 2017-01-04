# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
            