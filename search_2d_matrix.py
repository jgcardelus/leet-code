class Solution:
    def searchMatrix(self, matrix, target):
        flattened = []
        for row in matrix:
            flattened.extend(row)

        def binary_search(elems, target):
            print(elems)

            if len(elems) == 0:
                return False

            center = max(len(elems) // 2 - 1, 0)
            if elems[center] < target:
                return binary_search(elems[center+1:], target)
            elif elems[center] > target:
                return binary_search(elems[:center], target)
            else:
                return True

        return binary_search(flattened, target)

solver = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 61
print(solver.searchMatrix(matrix, target))
