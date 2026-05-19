# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0

        ans = dummy = ListNode()

        while l1 or l2:
            sumNode = ListNode()
            dummy.next = sumNode
            sumVal = carryOver
            print(f"****")

            if l1 and l2: 
                val1 = l1.val 
                val2 = l2.val
                sumVal += val1 + val2 
                l1 = l1.next
                l2 = l2.next
                print(f"val1: {val1}")
                print(f"val2: {val2}")
                print(f"carry over: {carryOver}")
                print(f"sum val: {sumVal}")
            elif l1: 
                val1 = l1.val
                sumVal += val1
                l1 = l1.next
                print(f"val1: {val1}")
                print(f"carry over: {carryOver}")
                print(f"sum val: {sumVal}")
            else: 
                val2 = l2.val
                sumVal += val2
                l2 = l2.next

                print(f"val2: {val2}")
                print(f"carry over: {carryOver}")
                print(f"sum val: {sumVal}")

            if sumVal>=10: 
                carryOver = 1
            else:
                carryOver = 0

            sumNode.val = sumVal % 10
            dummy = dummy.next
        
        if carryOver:
            extraNode = ListNode(1, None)
            dummy.next = extraNode
        
        
        return ans.next 