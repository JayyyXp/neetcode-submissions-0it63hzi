# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy.next
        curr = prev.next 
        while curr:
            tmp = curr.next
            gcd = max(prev.val, curr.val)
            while True:
                if prev.val % gcd == 0 and curr.val % gcd == 0:
                    break
                gcd -= 1
            print(gcd, prev.val // gcd, curr.val // gcd)
            new = ListNode(gcd,curr)
            prev.next = new
            prev = curr
            curr = tmp
        return dummy.next