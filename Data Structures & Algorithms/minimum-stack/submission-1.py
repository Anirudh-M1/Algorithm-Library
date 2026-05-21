class MinStack:

    def __init__(self):
        self.minElement  = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minElement and self.minElement[-1] < val: 
            self.minElement.append(self.minElement[-1]) 
        else: 
            self.minElement.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minElement.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElement[-1]
