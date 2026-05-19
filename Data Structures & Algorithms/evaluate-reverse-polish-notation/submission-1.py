class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = set(["+", "-", "*", "/"]) 
        stack = []
        for token in tokens: 
            if token in signs: 
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "*": 
                    stack.append(val1 * val2)
        
                elif token == "/":
                    stack.append(int(val1/val2))

                elif token == "+": 
                    stack.append(val1+val2)
                
                elif token == "-":
                    stack.append(val1 - val2)
            else: 
                stack.append(int(token))
        
        return stack[0]

        