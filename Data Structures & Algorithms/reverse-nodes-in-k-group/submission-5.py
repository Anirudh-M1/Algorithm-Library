# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        ans = dummy = ListNode()
        dummy.next = head
        while dummy.next:

            foundK = True
            tail = dummy
            for _ in range(k+1): 
                if tail:
                    tail = tail.next
                else:
                    foundK = False
                    return ans.next

            if foundK:
                dummy = self.reverse(dummy, k)

        return ans.next


    def reverse(self, p, k):
        a = curr = p.next 
        print(curr.val)

        prev = None
        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        

        p.next = prev
        a.next = curr

        return a
