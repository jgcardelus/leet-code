class Solution:
    def twoSum(self, numbers, target):
        lower = 0
        higher = len(numbers) - 1

        while lower < higher:
            current_sum = numbers[lower] + numbers[higher]
            if current_sum == target:
                return [lower + 1, higher + 1]

            if current_sum < target:
                lower += 1
            else:
                higher -= 1

        return [-1,-1]
