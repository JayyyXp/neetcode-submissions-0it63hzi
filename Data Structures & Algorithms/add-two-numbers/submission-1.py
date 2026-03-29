# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        ans_head = ans
        carry = 0
        while not(l1 is None and l2 is None): 
            
            val_l1 = l1.val if l1 is not None else 0
            val_l2 = l2.val if l2 is not None else 0
            new_val = val_l1 + val_l2 + carry
            if new_val >= 10:
                carry = new_val // 10
                ans.val = new_val % 10
            else:
                carry = max(carry-1,0)
                ans.val = new_val
            l1_next = l1.next if l1 is not None else None
            l2_next = l2.next if l2 is not None else None
            if l1_next is None and l2_next is None:
                break
            ans.next = ListNode()
            ans = ans.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            print(val_l1, val_l2, new_val, carry)
        if carry > 0:
            ans.next = ListNode()
            ans = ans.next
            ans.val += carry

        return ans_head