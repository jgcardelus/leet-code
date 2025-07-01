import heapq


class Solution:
    def findKthLargest(self, nums, k):
        nums=  [-nums[i] for i in range(len(nums))]
        heapq.heapify(nums)

        result = 1
        for _ in range(k):
            result = heapq.heappop(nums)

        return result * -1

nums = [3,2,3,1,2,4,5,5,6]
k = 4

solver = Solution()
print(solver.findKthLargest(nums,k))
