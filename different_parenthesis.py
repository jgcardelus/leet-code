class Solution:
    def diffWaysToCompute(self, expression):
        operators = "+-*"

        def apply(operator, lefts, rights):
            results = []
            for left in lefts:
                for right in rights:
                    if operator == "+":
                        results.append(left + right)
                    elif operator == "-":
                        results.append(left - right)
                    else:
                        results.append(left * right)
            return results

        def compute(expression):
            new_operations = []
            for i, letter in enumerate(expression):
                if letter in operators:
                    lefts = compute(expression[0:i])
                    rights = compute(expression[i+1:])
                    new_operations.extend(apply(letter, lefts, rights))

            if len(new_operations) == 0:
                return [int(expression)]

            return new_operations

        return compute(expression)

solver = Solution()
print(solver.diffWaysToCompute("2*3-4*5"))
