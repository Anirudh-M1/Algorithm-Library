# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNodeL1 = list1
        currentNodeL2 = list2
        ans = ListNode()
        ansCurrent = ans
        while currentNodeL1 or currentNodeL2: 
            print(ans.val)
            if currentNodeL1 is None: 
                ansCurrent.next = currentNodeL2
                break

            if currentNodeL2 is None: 
                ansCurrent.next = currentNodeL1
                break
            
            if currentNodeL1.val  < currentNodeL2.val : 
                ansCurrent.next = ListNode(currentNodeL1.val)
                currentNodeL1 = currentNodeL1.next
                ansCurrent = ansCurrent.next 
            else: 
                ansCurrent.next = ListNode(currentNodeL2.val)
                currentNodeL2 = currentNodeL2.next
                ansCurrent = ansCurrent.next 
            
    
        return ans.next