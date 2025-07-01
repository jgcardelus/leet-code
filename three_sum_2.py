class Solution:
    def threeSum(self, nums):
        nums.sort()

        lower, higher = 0, len(nums) -1

        solutions = set()

        while lower < higher:
            target = 0 - (nums[lower] + nums[higher])
            print(nums[lower], nums[higher], target)
            for i in range(lower+1, higher):
                if nums[i] == target:
                    solutions.add((nums[lower], nums[higher], nums[i]))
                    break

            if target > 0:
                lower += 1
            else:
                higher -= 1

        return list(solutions)

solver = Solution()
print(solver.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
