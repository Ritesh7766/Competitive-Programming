# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        trev = head
        while trev and trev.next:
            while trev and trev.next and trev.next.val == val:
                trev.next = trev.next.next
            trev = trev.next
        return head