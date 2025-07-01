class Solution:
    def longestConsecutive(self, nums):
        freqs = {}
        for i in nums:
            freqs[i] = 1
            # if i in freqs:
            #     freqs[i] += 1
            # else:

        max_num = max(nums)
        for i in range(0, max_num+1):
            prev = 0
            if i-1 in freqs.keys():
                prev = freqs[i-1]

            if i in freqs.keys():
                freqs[i] += prev

        return max(list(freqs.values()))

solver = Solution()
print(solver.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
