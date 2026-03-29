# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head):

            curr = head
            prev = None

            while curr:

                nxt = curr.next # store nxt bc curr will be flipped
                curr.next = prev # rev what curr is pointing to
                prev = curr # move prev
                curr = nxt # move curr

            return prev

        
        # gather all the starts
        starts = []
        curr = head
        counter = k
        n = 0
        while curr:
            nxt = curr.next
            if counter == 1:
                curr.next = None
            if counter == k:
                starts.append(curr)
            counter -= 1
            n += 1
            if counter == 0:
                counter = k
            curr = nxt
        excludeLast = False
        if n%k != 0:
            excludeLast = True
        #print([n.val for n in starts])
        for s in starts:
            print("start", s.val)
            curr = s
            l = []
            while curr:
                l.append(curr.val)
                curr = curr.next
            print(l)
        l = []
        for i, h in enumerate(starts):
            if excludeLast and i == len(starts)-1:
                l.append([h, None])
            else:
                rev_head = reverse(h)
                l.append([rev_head, h])
        ans = l[0][0]

        for i in range(1, len(l)):
            l[i-1][1].next = l[i][0]


        return ans