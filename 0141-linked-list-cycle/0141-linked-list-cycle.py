# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        p = head
        f = head

        while f and f.next:
            p = p.next
            f = f.next.next

            if p == f:
                return True
        
        return False