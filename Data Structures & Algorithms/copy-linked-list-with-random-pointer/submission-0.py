"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0)
        current_new = dummy
        current_old = head

        while current_old:
            current_new.next = Node(x=current_old.val)
            current_new = current_new.next
            current_old = current_old.next

        current_new = dummy.next
        current_old = head
        while current_old:
            if current_old.random is not None:
                
                current_new1 = dummy.next
                current_old1 = head
                #print('search', current_old.random.val)
                while current_old1 != current_old.random:
                    #print('curr', current_old1.val)
                    current_new1 = current_new1.next
                    current_old1 = current_old1.next          
                print('stopN', current_new1.val)
                print('stopO', current_old1.val)
                current_new.random = current_new1   

            current_new = current_new.next
            current_old = current_old.next
        #print('ans',dummy.next.val)

        return dummy.next
