class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_house(i):
            return nums[i] + decide_at_house(i+2)

        def skip_house(i):
            return decide_at_house(i+1)

        def decide_at_house(i):
            if i >= len(nums):
                return 0
            return max(rob_house(i), skip_house(i))

        return decide_at_house(0)

    def rob2(self, nums):
        if len(nums) == 1:
            return nums[0]

        solution = [0] * (len(nums)+2)
        for i in range(len(nums)-1,-1,-1):
            solution[i] = max(nums[i] + solution[i+2], solution[i+1])

        return solution[0]
