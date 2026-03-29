# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        newLL = ListNode()
        ans = newLL
        curr1 = list1
        curr2 = list2
        while True:
            if curr1 is not None and curr2 is not None:
                if curr1.val < curr2.val:
                    newLL.val = curr1.val
                    curr1 = curr1.next
                else:
                    newLL.val = curr2.val
                    curr2 = curr2.next
            elif curr1 is not None and curr2 is None:
                newLL.val = curr1.val
                curr1 = curr1.next
            elif curr2 is not None and curr1 is None:
                newLL.val = curr2.val
                curr2 = curr2.next
            else:
                break
            if curr1 is not None or curr2 is not None:
                newLL.next = ListNode()
                newLL = newLL.next  
                
        return ans
