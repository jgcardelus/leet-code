class Solution:
    def hIndex(self, citations):
        max_h = len(citations)
        citations.sort()
        for citation in citations:
            if max_h <= citation:
                return max_h
            max_h -= 1

        return 0

solver = Solution()
print(solver.hIndex([3,0,6,1,5]))
