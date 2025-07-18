class Solution:
    def minSubArrayLen(self, target, nums):
        min_len = len(nums) + 1
        left = 0

        acc = 0
        for right in range(len(nums)):
            acc += nums[right]

            while acc >= target:
               min_len = min(min_len, 1 + right - left)
               acc -= nums[left]
               left -= 1


    def minSubArrayLen2(self, target, nums):
        min_len = float("inf")
        left = 0
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                print(cur_sum, left, right)
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0

solver = Solution()
print(solver.minSubArrayLen(11, [1,2,3,4,5]))
