# time: 00:33:00

class Solution:
    def maxArea(self, height) -> int:
        max_area = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                current_length = j - i
                current_height = min(height[i], height[j])
                current_area = current_length * current_height
                if current_area > max_area:
                    max_area = current_area


        return max_area

solver = Solution()
assert solver.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert solver.maxArea([1,1]) == 1

print(solver.maxArea([1,8,6,2,5,4,8,3,7]))

# Actual O(n) solution
# max_area = 0
# left = 0
# right = len(height) - 1

# while left < right:
#     max_area = max(max_area, (right - left) * min(height[left], height[right]))

#     if height[left] < height[right]:
#         left += 1
#     else:
#         right -= 1

# return max_area
