"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.
"""

import math


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ret = 0

        def flood_fill(x, y, n=1):
            nonlocal ret
            if grid[x][y] < n:
                return
            grid[x][y] = n
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                row, col = len(grid), len(grid[0])
                if 0 <= new_x < row and 0 <= new_y < col:
                    flood_fill(new_x, new_y, n + 1)

        for x, line in enumerate(grid):
            for y, elt in enumerate(line):
                if elt == 1:
                    grid[x][y] = math.inf
                if elt == 2:
                    grid[x][y] = 1

        for x, line in enumerate(grid):
            for y, elt in enumerate(line):
                if elt == 1:
                    flood_fill(x, y)

        for x, line in enumerate(grid):
            if math.inf in line:
                return -1
            ret = max(ret, *line)
        return max(ret - 1, 0)
