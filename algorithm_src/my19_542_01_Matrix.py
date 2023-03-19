"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
"""
from ..tools.time_measure import time_measure

"""
# first version:
# fails miserably on last test: (~33sec exec time)
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

'''
# flood fill version
# deadlocks somehow idk :/
class Solution:
    @time_measure
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        def flood_fill(x, y, n):
            if mat[x][y] < n and not mat[x][y] == 1:
                return
            mat[x][y] = n
            if x > 0:               flood_fill(x - 1, y, n + 1)
            if y > 0:               flood_fill(x, y - 1, n + 1)
            if x < len(mat) - 1:    flood_fill(x + 1, y, n + 1)
            if y < len(mat[0]) - 1: flood_fill(x, y + 1, n + 1)
            return

        def is_neighbour(x, y, n):
            if x > 0 and mat[x - 1][y] == n: return True
            if y > 0 and mat[x][y - 1] == n: return True
            if x < len(mat) - 1 and mat[x + 1][y] == n: return True
            if y < len(mat[0]) - 1 and mat[x][y + 1] == n: return True
            return False

        d = dict()
        for x, line in enumerate(mat):
            for y, e in enumerate(line):
                if (e == 1):
                    if is_neighbour(x, y, 0):
                        d[str(x) + ',' + str(y)] = 1

        for key in d.keys():
            coords = key.split(',')
            coords = [int(c) for c in coords]
            mat[coords[0]][coords[1]] = 2
            flood_fill(coords[0], coords[1], 1)

        for key in d.keys():
            coords = key.split(',')
            coords = [int(c) for c in coords]
            mat[coords[0]][coords[1]] = 1

        return mat
'''


#   Idea of this version is to find set of squares
# on the border between 0s and 1s, then we start spreading all that border inside
#   We use cache_swapper to cache difference from step to step
# and delete unused values from outside of the border
class Solution:
    class CacheSwapper:
        def __init__(self, d):
            self.data = [d, None, None]
            self.ind = 0

        def get(self):
            return self.data[self.ind]

        def only_last(self):
            if self.data[(self.ind - 1) % 3] != None:
                return self.data[self.ind].difference(self.data[(self.ind - 1) % 3])
            else:
                return self.data[self.ind]

        def push(self, d: set):
            self.ind = (1 + self.ind) % 3
            self.data[self.ind] = d
            if self.data[(self.ind + 1) % 3] != None:
                self.data[self.ind] = self.data[self.ind].difference(self.data[(self.ind + 1) % 3])

    @time_measure
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        def is_neighbour(x, y, n):
            if x > 0 and mat[x - 1][y] == n: return True
            if y > 0 and mat[x][y - 1] == n: return True
            if x < len(mat) - 1 and mat[x + 1][y] == n: return True
            if y < len(mat[0]) - 1 and mat[x][y + 1] == n: return True
            return False

        d = set()
        for x, line in enumerate(mat):
            for y, e in enumerate(line):
                if (e == 1):
                    if is_neighbour(x, y, 0):
                        d.add((x, y))
                if (e == 0):
                    if is_neighbour(x, y, 1):
                        d.add((x, y))

        generation = 2
        cs = self.CacheSwapper(d)

        while True:
            found = 0
            d = cs.get()
            new_d = set()
            for e in cs.only_last():
                x, y = e[0], e[1]
                val = mat[x][y]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    row, col = len(mat), len(mat[0])
                    if 0 <= new_x < row and 0 <= new_y < col and mat[new_x][new_y] != 0 and not (new_x, new_y) in d:
                        new_d.add((new_x, new_y))
                        mat[new_x][new_y] = generation
                        found += 1

            d = d.union(new_d)
            cs.push(d)
            generation += 1
            if found == 0:
                break

        return mat
