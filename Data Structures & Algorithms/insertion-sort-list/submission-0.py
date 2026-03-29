# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(val=-5001)
        dummy = ans
        
        while head:
            dummy = ans
            nxt = head.next

            while dummy.next:
                if head.val < dummy.next.val:
                    break
                dummy = dummy.next
            store = dummy.next
            dummy.next = head
            head.next = store

            head = nxt

        return ans.next