# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None or l2 is None:
            return l1 or l2
            
        if l1.val > l2.val:
            l1, l2 = l2, l1
            
        l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1 or l2
                
                
            
               
        