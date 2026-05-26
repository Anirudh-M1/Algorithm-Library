class Node:
        def __init__(self, val = 0,key = 0, next = None, prev = None): 
            self.val = val 
            self.key = key
            self.next = next
            self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

        self.cache = {} # key to node

    def get(self, key: int) -> int:
        # if node already exists
        if key in self.cache: 
            node = self.cache[key]
            self.removeNode(node)
            self.insertAtHead(node)
            return node.val

        #if node does not exist
        return -1

    def put(self, key: int, value: int) -> None:
        #if node aready exists
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)

        #if node doesnt exist 
        else:
            print(value)
            if len(self.cache) >= self.capacity:
                print("capacity exceded")
                node = self.removeFromTail()
                del self.cache[node.key]

            node = Node(value, key)
            self.cache[key] = node

        #always move to head
        self.insertAtHead(node)

    def removeNode(self, node): 
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeFromTail(self) -> node: 
        node = self.tail.prev
        prevNode = node.prev
        prevNode.next = self.tail
        self.tail.prev = prevNode
        return node

    def insertAtHead(self, node):
        nextNode = self.head.next 
        node.next = nextNode
        node.prev = self.head
        self.head.next = node
        nextNode.prev = node






