# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = cur = ListNode() 
        while lists: 
            minVal = float("inf")
            minIdx = float("inf") 
            for idx, node in enumerate(lists):
                if node and node.val < minVal: 
                    minVal = node.val
                    minIdx = idx

            if minVal == float("inf"):
                return ans.next

            cur.next = lists[minIdx]
            lists[minIdx] = lists[minIdx].next
            cur = cur.next