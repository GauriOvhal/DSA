# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):

        slow , fast = head , head.next

        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next

        
        second = slow.next

        previous = slow.next = None

        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp


        #merge
        first , second = head ,previous

        while second:
            t1 , t2 = first.next , second.next

            first.next = second
            second.next = t1
            first = t1
            second = t2
            
