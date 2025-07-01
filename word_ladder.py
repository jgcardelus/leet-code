#
# Crear grafo, donde nodos estan conectados sin son transformacion
# Ejecuto BFS, para encontrar shorter route entre begin y end
#

from collections import deque


class Solution:
    def word_ladder(self, start, end, word_dict):
        # O(n)
        if end not in word_dict:
            return 0

        def is_transformation(a, b):
            different_letters = 0
            for cursor in range(len(a)):
                if a[cursor] != b[cursor]:
                    different_letters += 1

            return different_letters == 1

        # Construct graph
        graph = {}
        word_dict.append(start)
        # O(n*n*m)
        for word in word_dict:
            transformations = []

            for target in word_dict:
                if word == target:
                    continue

                if is_transformation(word, target):
                    transformations.append(target)

            graph[word] = transformations

        # BFS
        # [{from, to}]

        queue = deque([(start, to) for to in graph[start]])
        visited = {}
        visited[start] = 1

        # O(v*e) -> O(m*n)
        while queue:
            prev, to = queue.popleft()

            if to in visited:
                continue

            visited[to] = visited[prev] + 1

            if to == end:
                break

            queue.extend([(to, neighbor) for neighbor in graph[to]])

        if end not in visited:
            return 0

        return visited[end]

solver = Solution()
print(solver.word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(solver.word_ladder("hit", "cog", ["hot","aaa","cog"]))
print(solver.word_ladder("hit", "cog", ["hot","aaa"]))
