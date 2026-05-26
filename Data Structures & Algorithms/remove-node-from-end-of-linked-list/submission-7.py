# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        pioneer = dummy
        pioneer.next = head
        for i in range(n+1): 
            pioneer = pioneer.next 
        

        beforeRemove = dummy
        while pioneer: 
            beforeRemove = beforeRemove.next
            pioneer = pioneer.next
        print(beforeRemove.val)
        beforeRemove.next = beforeRemove.next.next 

        return dummy.next
