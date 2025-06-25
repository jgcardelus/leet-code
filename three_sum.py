class Solution:
    def threeSum(self, nums):
        data = list(sorted(nums))
        results = set()

        for i in range(len(data)):
            if i > 0 and data[i-1] == data[i]:
                continue

            a = i + 1
            b = len(data) - 1

            while a < b:
                if data[i] + data[a] + data[b] == 0:
                    results.add((data[i], data[a], data[b]))
                    a += 1
                else:
                    if (data[a] + data[b]) > (0 - data[i]):
                        b -= 1
                    else:
                        a += 1

        return list(results)

solver = Solution()
print(solver.threeSum([-1,0,1,2,-1,-4]))
print(solver.threeSum([0,1,1]))
print(solver.threeSum([0,0,0]))
