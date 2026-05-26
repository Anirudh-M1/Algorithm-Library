# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midpoint
        fast = head
        slow = head
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        
        h2 = slow.next
        slow.next = None

        #reverse linked list

        prev = None
        cur = h2
        while cur: 
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt
        
        
        h1 = head 
        h2 = prev
        
        while h2:
            nxt1 = h1.next
            nxt2 = h2.next
            
            h1.next = h2
            h2.next = nxt1
            
            h1 = nxt1
            h2 = nxt2
           


