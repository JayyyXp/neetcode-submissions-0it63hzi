# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        f = head
        l = 0
        while f:
            l += 1
            f = f.next
        if l < 2 or k == 0 or k == l:
            return head
        k = l - (k % l) # mod the list len
        print(k)
        f = head
        prev = None 
        newHead = head
        for _ in range(k):
            prev = newHead
            newHead = newHead.next 
        prev.next = None
        last = newHead
        while last.next:
            last = last.next
        last.next = f 

        return newHead