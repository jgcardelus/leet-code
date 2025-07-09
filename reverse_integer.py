class Solution:
    def reverse(self, x):
        x = str(x)
        reversed_num = ""

        start = 0
        if x[start] == "-":
            reversed_num += "-"
            start += 1

        for i in range(len(x)-1,start-1,-1):
            reversed_num += x[i]

        try:
            return int(reversed_num)
        except ValueError:
            return 0

solver = Solution()
print(solver.reverse(123))
print(solver.reverse(-123))
print(solver.reverse(-120))
