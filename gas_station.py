class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_gas < total_cost:
            return -1

        start = (len(gas) - 1, gas[-1] - cost[-1])
        acc = 0
        for i in range(len(gas) - 1, -1, -1):
            acc += gas[i] - cost[i]
            if acc > start[1]:
                start = (i, acc)

        return start[0]

solver = Solution()
print(solver.canCompleteCircuit([2,3,4], [3,4,3]))
