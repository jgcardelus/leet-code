from collections import deque

class Solution:
    def permute(self, nums):
        permutations = []
        def explore(nums, acc):
            if len(nums) == 0:
                permutations.append(acc[:])
                return

            for i in range(len(nums)):
                next = nums.popleft()
                acc.append(next)
                explore(nums, acc)
                acc.remove(next)
                nums.append(next)

        nums = deque(nums)
        explore(nums, [])
        return permutations

solver = Solution()
print(solver.permute([1]))
