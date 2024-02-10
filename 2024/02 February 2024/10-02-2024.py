"""

Author : Shuvam Kumar Singh
Date : 10/02/2024
Problem : Number of paths in a matrix with k coins
Difficulty : Medium

"""


class Solution:
    def numberOfPath (self, n, k, arr):
        # code here
        memo = [[[-1] * (k + 1) for _ in range(n)] for _ in range(n)]

        def go(row, col, remaining):
            if row < 0 or col < 0:
                return 0
            if row == 0 and col == 0:
                return int(remaining == arr[0][0])
            if memo[row][col][remaining] != -1:
                return memo[row][col][remaining]

            paths = 0
            if remaining >= arr[row][col]:
                paths = go(row - 1, col, remaining - arr[row][col]) + go(row, col - 1, remaining - arr[row][col])

            memo[row][col][remaining] = paths
            return paths

        return go(n - 1, n - 1, k)
