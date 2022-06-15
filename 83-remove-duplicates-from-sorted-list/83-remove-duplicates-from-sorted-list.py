# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trev = head
        while trev and trev.next:
            while trev and trev.next and trev.val == trev.next.val:
                trev.next = trev.next.next
            trev = trev.next
        return head