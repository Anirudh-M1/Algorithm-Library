# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        lengthList = 0
        lenHead = head
        while lenHead: 
            lenHead= lenHead.next
            lengthList +=1 
        
        print(f"length of list is: {lengthList}")

        if lengthList == 1: 
            return None

        removeIdx = lengthList - n
        print(f"remove Index is {removeIdx}")

        rmPtr = head
        for i in range(removeIdx - 1): 
            rmPtr = rmPtr.next
        
        if rmPtr == head and removeIdx == 0: 
            head = head.next
        else:
            rmPtr.next = rmPtr.next.next

            # print("head", end=" ")
            # hprint =head
            # while hprint: 
            #     print(hprint.val, end="->")
            #     hprint = hprint.next
            # print("None")
        return head
