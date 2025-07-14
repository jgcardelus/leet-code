class Solution:
    def minimumTotal(self, triangle):
        base_length = len(triangle[-1])
        interim_sums = [[0] * base_length for _ in range(len(triangle))]

        for level in reversed(range(len(triangle))):
            for i in reversed(range(len(triangle[level]))):
                min_next_level = 0
                if level < len(triangle) - 1:
                    min_next_level = min(interim_sums[level+1][i], interim_sums[level+1][i+1])
                interim_sums[level][i] = triangle[level][i] + min_next_level

        return interim_sums[0][0]

solver = Solution()
