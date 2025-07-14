class Solution:
    def lengthOfLIS(self, nums):
        intermediate_lis = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            value = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    value = max(value, 1+intermediate_lis[j])
            intermediate_lis[i]=value
        return max(intermediate_lis)

solver = Solution()
print(solver.lengthOfLIS([7,7,7,7,7,7,7]))
