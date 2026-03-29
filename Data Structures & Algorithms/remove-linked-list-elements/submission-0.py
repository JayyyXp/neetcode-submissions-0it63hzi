# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(val=-1, next=head)
        tmp = dummy
        while tmp:
            nxt = tmp.next
            while nxt and nxt.val == val:
                nxt = nxt.next
            tmp.next = nxt
            tmp = tmp.next
        return dummy.next