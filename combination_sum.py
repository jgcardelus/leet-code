class Solution:
    def combination_sum(self, candidates, target):
        combinations = []

        def explore(combination, total):
            if total == target:
                combinations.append(combination)
                return
