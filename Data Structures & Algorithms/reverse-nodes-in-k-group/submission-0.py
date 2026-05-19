class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # Check if there are k nodes ahead
            frontierPtr = prev_group
            for _ in range(k):
                frontierPtr = frontierPtr.next
                if not frontierPtr:
                    return dummy.next  # Not enough nodes

            next_group = frontierPtr.next

            # Reverse current k-group
            start = prev_group.next
            prev_group.next = self.reverse(start, k, frontierPtr.next)

            # Move prev_group to the tail of reversed group (which is start)
            prev_group = start

    def reverse(self, head, k, kth):
        prev = kth
        for _ in range(k):
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev
