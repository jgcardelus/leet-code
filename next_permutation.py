## WARN: Not solved!

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        curr, peek = 0, 1

        while peek < len(nums):
            if nums[curr] < nums[peek]:
                # Flip
                helper = nums[curr]
                nums[curr] = nums[peek]
                nums[peek] = helper
                nums[peek:].sort()
                return
            curr, peek = peek, peek + 1

        nums.sort()

solver = Solution()
a = [3,2,1]
b = [1,1,5]

solver.nextPermutation(a)
solver.nextPermutation(b)
print(a)
print(b)
