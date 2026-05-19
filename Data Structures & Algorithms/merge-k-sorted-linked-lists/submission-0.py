# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ans = ListNode()
        valsPresent = True

        while dummy:  
            nextSmallest = float("inf")
            nextSmallestNode = None
            nextSmallestIdx = 0
            valsPresent = False
            
            for i, linkedListHead in enumerate(lists):
                if linkedListHead and linkedListHead.val < nextSmallest:
                    nextSmallestNode = linkedListHead 
                    nextSmallest = nextSmallestNode.val
                    nextSmallestIdx = i
                    valsPresent = True
            #update the corresponding list
            if nextSmallestNode: 
                lists[nextSmallestIdx] = nextSmallestNode.next

            dummy.next = nextSmallestNode
            dummy = dummy.next 
        
        return ans.next
        
