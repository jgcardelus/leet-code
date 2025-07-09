import heapq

## Not resolved !!

class Solution:
    def maxEvents(self, events):
        events.sort()

        min_heap = []
        i = 0
        count = 0

        last_day = max(end for _, end in events)

        for day in range(1, last_day+1):
            while i < len(events) and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                count += 1

            if i == len(events) and not min_heap:
                break

        return count
