# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def delete(node):
            flg = False
            while node and node.next and node.val == node.next.val:
                node.next = node.next.next
                flg = True
            return flg
                
        while head:
            if delete(head):
                head = head.next
            else: break
        
        trev, prev = head, None
        while trev:
            if delete(trev):
                prev.next = prev.next.next
            else: prev = trev
            trev = trev.next
                
        return head
                        
            
        