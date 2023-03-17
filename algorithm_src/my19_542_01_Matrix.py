"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
"""
from ..tools.time_measure import time_measure

"""
first version:
fails miserably on last test: (~33sec exec time)
class Solution:
    @time_measure
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        def is_neighbour(x, y, n):
            if x > 0 and mat[x - 1][y] == n: return True
            if y > 0 and mat[x][y - 1] == n: return True
            if x < len(mat) - 1    and mat[x + 1][y] == n: return True
            if y < len(mat[0]) - 1 and mat[x][y + 1] == n: return True
            return False

        to_find = 1
        while True:
            found = 0
            for x, line in enumerate(mat):
                for y, e in enumerate(line):
                    if (e == to_find) and (not is_neighbour(x, y, to_find - 1)):
                        mat[x][y] = to_find + 1
                        found += 1
            to_find += 1
            if found == 0:
                return mat
"""

class Solution:
    @time_measure
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        class Solution:
            @time_measure
            def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

                def in_bounds(x, y):
                    if x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0]): return True
                    return False
                def is_neighbour(x, y, n):
                    if x > 0 and mat[x - 1][y] == n: return True
                    if y > 0 and mat[x][y - 1] == n: return True
                    if x < len(mat) - 1 and mat[x + 1][y] == n: return True
                    if y < len(mat[0]) - 1 and mat[x][y + 1] == n: return True
                    return False
                def get_neighbours(x, y):
                    n = mat[x][y]
                    d = dict()
                    if x > 0 and mat[x - 1][y] == n: d[(x, y)] = n
                    if y > 0 and mat[x][y - 1] == n: return True
                    if x < len(mat) - 1 and mat[x + 1][y] == n: return True
                    if y < len(mat[0]) - 1 and mat[x][y + 1] == n: return True
                    return False

                d = dict()
                for x, line in enumerate(mat):
                    for y, e in enumerate(line):
                        if (e == 1) and is_neighbour(x, y, 0):
                            d[(x, y)] = 1
                to_find = 1
                for key, val in d:
                    n =
