from collections import deque


class Solution:
    def findRedundantConnection(self, edges):
        graph = {}
        redundant = None
        def has_cycle(start, graph):
            visited = set([start])
            neighbors = deque([[start, neighbor] for neighbor in graph[start]])

            while neighbors:
                [og, next] = neighbors.popleft()
                if next == start:
                    return True

                if next in visited:
                    continue

                visited.add(next)
                next_neighbors = graph[next]
                for next_neighbor in next_neighbors:
                    if next_neighbor != og:
                        neighbors.appendleft([next, next_neighbor])

            return False

        for start, end in edges:
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)

            if end not in graph:
                graph[end] = [start]
            else:
                graph[end].append(start)

            if has_cycle(start, graph):
                graph[start].remove(end)
                graph[end].remove(start)
                redundant = [start, end]

        return redundant


solver = Solution()
print(solver.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
