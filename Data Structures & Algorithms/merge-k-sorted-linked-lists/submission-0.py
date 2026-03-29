# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = ListNode()
        ans = temp
        while True:
            counter = 0
            minVal = float('inf')
            minIdx = -1
            for i, l in enumerate(lists):
                if not l:
                    counter += 1
                    continue
                if l.val < minVal:
                    minVal = l.val
                    minIdx = i
            print(minIdx, minVal)
            # done, all list items are pointing None
            if counter == len(lists):
                break
            # move minIdx list by one
            lists[minIdx] = lists[minIdx].next

            temp.next = ListNode(val=minVal)
            temp = temp.next
            



        return ans.next