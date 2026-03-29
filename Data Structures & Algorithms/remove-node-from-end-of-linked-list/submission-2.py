# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        fromStart = len(nodes) - n 
        if fromStart == 0:
            return head.next
        if fromStart + 1 > len(nodes)-1:
            nodes[fromStart - 1].next = None
        else:
            nodes[fromStart - 1].next = nodes[fromStart+1]
            

        return head