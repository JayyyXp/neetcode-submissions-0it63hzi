# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node before reversal starts
        for _ in range(1, left):
            prev = prev.next

        # Start reversal
        curr = prev.next
        prevNew = None
        
        for _ in range(left, right + 1):
            temp = curr.next
            curr.next = prevNew
            prevNew = curr
            curr = temp

        # Connect the parts:
        # prev -> prevNew (reversed head)
        # tail of reversed (prev.next) -> curr (remainder of list)
        tail = prev.next
        tail.next = curr
        prev.next = prevNew

        return dummy.next