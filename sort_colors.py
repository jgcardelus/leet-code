class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        last_red, last_blue = 0, len(nums) - 1
        cursor = 0

        while cursor <= last_blue:
            while nums[cursor] == 0 and cursor >= last_red:
                helper = nums[last_red]
                nums[last_red] = nums[cursor]
                nums[cursor] = helper
                last_red += 1

            while nums[cursor] == 2 and cursor <= last_blue:
                helper = nums[last_blue]
                nums[last_blue] = nums[cursor]
                nums[cursor] = helper
                last_blue -= 1

            cursor += 1

solver = Solution()
a = [2,0,2,1,1,0]
solver.sortColors(a)
print(a)
