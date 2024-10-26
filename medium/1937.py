from typing import List


class Solution:
    # slow sollution
    # def maxPoints(self, points: List[List[int]]) -> int:
    #     n = len(points)
    #     m = len(points[0])
    #     max_matrix = [[0 for j in range(m)] for i in range(n)]
    #     max_matrix[0] = [points[0][i] for i in range(m)]
    #     for i in range(1, n):
    #         for j in range(m):
    #             for k in range(m):
    #                 max_matrix[i][j] = max(max_matrix[i][j], max_matrix[i - 1][k] - abs(j - k) + points[i][j])
    #     return max(max_matrix[n - 1])

    # original
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        max_matrix = [[(0, j) for j in range(m)] for i in range(n)]
        max_matrix[0] = [(points[0][i], i) for i in range(m)]
        for i in range(1, n):
            max_matrix[i - 1].sort(key=lambda item: item[0])
            for j in range(m):
                pass
        # return max(max_matrix[n - 1])


points = [[0]]
print(Solution().maxPoints(points))
