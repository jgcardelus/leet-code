class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals[:]

        merged = []
        intervals.sort()

        start, end = intervals[0][0], intervals[0][1]

        for next_start, next_end in intervals[1:]:
            if end >= next_start:
                # Next interval, overlaps
                end = max(next_end, end)
            else:
                # Next interval does NOT overlap
                merged.append([start, end])
                start, end = next_start, next_end

        merged.append([start, end])

        return merged

solver = Solution()
print(solver.merge([[1,3],[2,6],[8,10],[15,18]]))
