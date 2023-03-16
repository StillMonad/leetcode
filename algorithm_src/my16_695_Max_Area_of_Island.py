class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        def fill(x, y):
            nonlocal grid
            c = 0
            if grid[x][y] < 0:
                return 0
            if grid[x][y] == 1:
                grid[x][y] = -1
                c += 1
                if x > 0: c += fill(x - 1, y)
                if y > 0: c += fill(x, y - 1)
                if x < (len(grid) - 1): c += fill(x + 1, y)
                if y < (len(grid[0]) - 1): c += fill(x, y + 1)
            return c

        m = 0
        for i, v in enumerate(grid):
            for j, v in enumerate(grid[0]):
                m = max(m, fill(i, j))

        return m
