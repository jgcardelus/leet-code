class Solution:
    def jump(self, nums):
        costs = [len(nums)] * len(nums)
        costs[0] = 0

        for i, max_jump in enumerate(nums):
            j = min(i + max_jump, len(nums) - 1)
            cost = costs[i] + 1

            for z in range(j, i, -1):
                if cost < costs[z]:
                    costs[z] = cost

        return costs[-1]

solver = Solution()

print(solver.jump([2,3,1,1,4]))
