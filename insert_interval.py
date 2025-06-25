class Solution:
    def insert(self, intervals, newInterval):
        merged_intervals = []
        inserted_start = False
        inserted_end = False

        next_interval = [0, 0]
        for i in range(len(intervals)):
            current_interval = intervals[i]
            if not inserted_start:
                if newInterval[0] < current_interval[0]:
                    next_interval[0] = newInterval[0]
                    inserted_start = True
                elif newInterval[0] > current_interval[0] and newInterval[0] <= current_interval[1]:
                    next_interval[0] = current_interval[0]
                    inserted_start = True
                elif newInterval[0] > current_interval[1]:
                    merged_intervals.append(current_interval)
            elif not inserted_end:
                if newInterval[1] < current_interval[0]:
                    inserted_end = True
                    next_interval[1] = newInterval[1]
                    merged_intervals.append(next_interval)
                    merged_intervals.append(current_interval)
                elif newInterval[1] >= current_interval[0] and newInterval[1] <= current_interval[1]:
                    inserted_end = True
                    next_interval[1] = current_interval[1]
                    merged_intervals.append(next_interval)
            else:
                merged_intervals.append(current_interval)

        if not inserted_end:
            next_interval[1] = newInterval[1]
            merged_intervals.append(next_interval)

        return merged_intervals

solver = Solution()
print(solver.insert([[1,3],[6,9]], [2,5]))
