# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0 
        lenHead = head
        while lenHead: 
            lenHead = lenHead.next
            length+=1 

        
        h1, h2 = head, head

        for _ in range(length//2 - 1):
            h2 = h2.next
        nextNode = h2.next
        h2.next = None
        h2 = nextNode

        prev = None
        while h2:   
            nextNode = h2.next
            h2.next = prev 

            prev = h2 
            h2 = nextNode

        h2 = prev 

        dummy = ans = ListNode()
        while h1 and h2: 
            dummy.next = h1 
            print(h1.val)
            h1 = h1.next
            dummy = dummy.next
            dummy.next = h2
            print(h2.val)
            h2= h2.next
            dummy = dummy.next
        
        dummy.next = h1 or h2
        

        # print("h1", end=" ")
        # h1print =h1
        # while h1print: 
        #     print(h1print.val, end="->")
        #     h1print = h1print.next
        # print("None")

