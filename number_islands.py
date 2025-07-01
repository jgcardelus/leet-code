class Solution:
    def addIfNeighbor(self, i, j, grid, neighbors):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
            if grid[i][j] == "1":
                neighbors.append([i,j])

        return neighbors

    def findNeighbors(self, i, j, grid):
        neighbors = []
        for a in [-1,0,1]:
            for b in [-1,0,1]:
                if abs(a)==abs(b):
                    continue
                neighbors = self.addIfNeighbor(i+a,j+b,grid,neighbors)

        return neighbors

    def exploreIsland(self, i, j, grid):
        grid[i][j] = "2"
        neighbors = self.findNeighbors(i, j, grid)
        for y,x in neighbors:
            self.exploreIsland(y, x, grid)

    def numIslands(self, grid):
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell = grid[i][j]
                if cell == "1":
                    # Explore islands
                    self.exploreIsland(i,j,grid)
                    islands+=1

        return islands

solver = Solution()
print(solver.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]))

print(solver.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]))

print(solver.numIslands([
    ["0","1","0"],["1","0","1"],["0","1","0"]
]))
