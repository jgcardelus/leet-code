from collections import deque


class Solution:
    def isMutation(self, a, b):
        changes = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                changes += 1

        return changes == 1

    def minMutation(self, startGene, endGene, bank):
        if endGene not in bank:
            return -1

        graph = {}
        genes = [startGene] + bank
        costs = {}

        for gene in genes:
            graph[gene] = []
            costs[gene] = 0

            for other in genes:
                if gene == other:
                    continue

                if self.isMutation(gene, other):
                    graph[gene].append(other)

        queue = deque([startGene])
        while queue:
            next = queue.popleft()
            neighbors = graph[next]

            for neighbor in neighbors:
                if costs[neighbor] > 0:
                    continue

                costs[neighbor] = costs[next] + 1

                if neighbor == endGene:
                    costs[neighbor] = costs[next] + 1
                    break

                queue.append(neighbor)

        min_mutations = costs[endGene]
        if min_mutations == 0:
            return -1

        return min_mutations

    def minMutation2(self, startGene, endGene, bank):
        queue = deque([[startGene, 0]])
        visited = set()

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for neighbor in bank:
                if self.isMutation(gene, neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor, mutations+1])

        return -1

solver = Solution()
print(solver.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))
