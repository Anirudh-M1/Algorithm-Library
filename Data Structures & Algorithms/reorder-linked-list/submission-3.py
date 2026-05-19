# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head, head

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        
        h1 = head
        h2 = slow.next
        slow.next = None


        #Step 3 Reverse Second Half of List
        prev = None
        while h2:   
            nextNode = h2.next
            h2.next = prev 

            prev = h2 
            h2 = nextNode
        h2 = prev 

        # Step 4: Merge lists
        first, second = h1, h2
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        