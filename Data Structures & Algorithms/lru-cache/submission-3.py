class ListNode: 
    def __init__(self, key = None, value = None, nextPtr = None): 
        self.key = key
        self.value = value
        self.next = nextPtr
        self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeHash = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.nodeHash: 
            return -1

        node = self.nodeHash[key]
        self._remove(node)
        self._insert_at_head(node)

        return node.value

    def put(self, key: int, value: int) -> None: 
        if key in self.nodeHash: 
            node = self.nodeHash[key]
            node.value = value
            self._remove(node)
            self._insert_at_head(node)
            return

        if len(self.nodeHash) + 1 > self.capacity:
           self._remove(self.tail.prev)

        newNode = ListNode(key , value)
        self.nodeHash[key] = newNode
        self._insert_at_head(newNode)

    def _remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del self.nodeHash[node.key] 
        
    def _insert_at_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.nodeHash[node.key] = node
        
    

