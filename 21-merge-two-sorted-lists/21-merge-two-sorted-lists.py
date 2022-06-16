# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        
        left, right = list1, list2
        if left.val <= right.val: 
            head, left = left, left.next
        else: head, right = right, right.next
        
        trev = head
        while left and right:
            if left.val <= right.val: 
                trev.next, left = left, left.next
            else: trev.next, right = right, right.next
            trev = trev.next
        
        if left: trev.next = left
        if right: trev.next = right
            
        return head
        
        