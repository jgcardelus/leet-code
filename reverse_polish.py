
class Solution:
    def is_operator(self, token):
        return token in "+-/*"

    def calculate(self, left, right, operator):
        if operator == "+":
            return left + right
        if operator == "-":
           return left - right
        if operator == "*":
           return left * right
        if operator == "/":
            return int(left / right)

    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if not self.is_operator(token):
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(self.calculate(left, right, token))

        return stack


solver = Solution()
# print(solver.evalRPN(["2","1","+","3","*"]))
# print(solver.evalRPN(["4","13","5","/","+"]))
print(solver.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
