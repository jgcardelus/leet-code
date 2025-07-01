class Solution:
    def addToGraph(self, start, end, value, graph):
        if start in graph:
            graph[start].append([end, value])
        else:
            graph[start] = [[end, value]]

    def buildGraph(self, equations, values):
        graph = {}
        for i, [start, end] in enumerate(equations):
            value = values[i]
            reversed = 1/value
            self.addToGraph(start, end, value, graph)
            self.addToGraph(end, start, reversed, graph)

        return graph

    def calculate(self, query, graph, visited):
        start, end = query

        if start not in graph:
            return -1

        if start == end:
            return 1

        neighbors = graph[start]
        visited.add(start)

        for name, cost in neighbors:
            print(start, name, visited)
            if name in visited:
                continue
            if name == end:
                return cost
            else:
                result = self.calculate([name, end], graph, visited)
                if result != -1:
                    return result*cost

        return -1

    def calcEquation(self, equations, values, queries):
        graph = self.buildGraph(equations, values)
        print(graph)

        results = []
        for query in queries:
            visited = set()
            result = self.calculate(query, graph, visited)
            results.append(result)

        return results

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x2","x4"]]

solver = Solution()
print(solver.calcEquation(equations, values, queries))
