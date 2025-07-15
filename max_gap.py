## The min gap numbers is ceiling([max-min]/(N-1))
# This is wrong, use bucket sort

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        min_num, max_num = min(nums), max(nums)

        buckets = [-1] * (1+max_num - min_num)

        for num in nums:
            buckets[num - min_num] = 1

        max_diff = 0
        start_idx, end_index = -1, 0

        while end_index < len(nums):
            if buckets[end_index] == 1:
                if start_idx == -1:
                    start_idx = end_index
                else:
                    max_diff = max(1+end_index - start_idx, max_diff)
                    start_idx = end_index

            end_index += 1

        return max_diff

solver = Solution()
print(solver.maximumGap([3,6,9,1]))
