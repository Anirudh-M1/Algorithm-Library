# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = windowStart = ListNode()
        windowStart.next = head    

        while True:
            windowEnd = windowStart
            for i in range(k): 
                if windowEnd.next:
                    windowEnd = windowEnd.next
                else: 
                    return ans.next   

            curGroupStart = windowStart.next
            nextGroupStart = windowEnd.next

            windowStart.next = self.reverseList(curGroupStart,nextGroupStart) 

            windowStart = curGroupStart


    def printList(self, head): 
        cpy = head

        while cpy:
            print(cpy.val, end = " ")
            cpy= cpy.next
    

    def reverseList(self, head , tail): 
        cur = head
        prev = tail
        while cur!=tail: 
            nextNode = cur.next
            cur.next = prev

            prev = cur
            cur = nextNode
        return prev