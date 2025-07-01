class Solution:
    def maxArea(self, height):
        lower, higher = 0, len(height)

        max_area = 0

        while lower < higher:
            current_area = min(height[lower], height[higher]) * (higher-lower)
            max_area = max(max_area, current_area)

            if height[lower] > height[higher]:
                higher -= 1
            else:
                lower += 1

        return max_area
