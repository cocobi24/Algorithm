# https://neetcode.io/problems/search-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        idx = 0
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                idx = i
                break
        return target in matrix[idx]