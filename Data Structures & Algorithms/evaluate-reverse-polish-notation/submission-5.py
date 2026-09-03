class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:


            if token == "+":
                b = stack.pop()
                a = stack.pop()
                tempSum = a + b
                stack.append(tempSum)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                tempSum = a - b
                stack.append(tempSum)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                tempSum = a * b
                stack.append(tempSum)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                tempSum = int(a/b)
                stack.append(tempSum)
            else:
                stack.append(int(token))
        return stack.pop()