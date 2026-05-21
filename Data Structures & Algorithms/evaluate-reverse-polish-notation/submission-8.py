class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        
        for t in tokens:    
            if t!= "+" and t!= "-" and t!= "*" and t!= "/" : 
                print(t)
                stack.append(t)
            else: 
                num2 = int(float(stack.pop()))
                num1 = int(float(stack.pop()))

                if t == "+": 
                    stack.append(str(num1 + num2))
                elif t=="-":
                    stack.append(str(num1 - num2))
                elif t == "*": 
                    stack.append(str(num1 * num2))
                elif t == "/":
                    stack.append(str(num1 / num2))
            print(stack)
        return int(float(stack.pop()))