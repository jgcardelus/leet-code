class Solution:
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(0, len(nums)-1):
            left[i+1] = nums[i] * left[i]

        for i in range(len(nums) - 1, 0, -1):
            right[i-1]= nums[i] * right[i]

        for i in range(len(nums)):
            nums[i] = left[i] * right[i]

        return nums


solver = Solution()
print(solver.productExceptSelf([1,2,3,4]))
