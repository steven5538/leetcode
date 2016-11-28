# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def checkUpBound(self, l1):
        if l1.val >= 10:
                l1.val -= 10
                
                if l1.next is None:
                    t = ListNode(1)
                    l1.next = t
                else:
                    l1.next.val += 1
        
    def addTwoNumbers(self, l1, l2):
        n = l1
        prev = None
        while l1 is not None and l2 is not None:
            l1.val += l2.val
            self.checkUpBound(l1)
            
            prev = l1
            l1 = l1.next
            l2 = l2.next
            
        if l1 is None:
            l1 = prev
            l1.next = l2
                
        if l2 is None:
            while l1 is not None:
                self.checkUpBound(l1)
                l1 = l1.next
            
        return n
