# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = dummy = ListNode()
        carryOver = 0
        while (l1 or l2 or carryOver): 
            s = carryOver

            if l1 and l2: 
                s += l1.val+l2.val
                l1= l1.next
                l2= l2.next
            elif l1:
                s += l1.val
                l1 = l1.next
            elif l2: 
                s += l2.val
                l2 = l2.next
            
            if s >= 10:
                carryOver = 1
                s = s % 10
            else: 
                carryOver = 0
            
            dummy.next = ListNode(s)
            dummy = dummy.next
        
        return ans.next