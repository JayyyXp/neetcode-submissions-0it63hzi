# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        helper = []
        curr = head
        while curr is not None:
            helper.append(curr)
            curr = curr.next
        curr = head
        print(curr.val)

        i, j = 0, len(helper) - 1
        while i < j:
            helper[i].next = helper[j]
            i += 1
            if i >= j:
                break
            helper[j].next = helper[i]
            j -= 1
        
        helper[i].next = None