class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        filled = 1
        color_to_fill = image[sr][sc]
        if color_to_fill == color:
            return image
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == color:
                    image[i][j] = -1
        image[sr][sc] = color

        while True:
            if filled == 0:
                break
            filled = 0
            for i in range(len(image)):
                for j in range(len(image[0])):
                    k = image[i][j]
                    im = image[i][j]
                    if image[i][j] == color:
                        if i > 0 and (image[i - 1][j] == color_to_fill):
                            image[i - 1][j] = color
                            filled += 1
                        if i < (len(image) - 1) and (image[i + 1][j] == color_to_fill):
                            image[i + 1][j] = color
                            filled += 1
                        if j > 0 and (image[i][j - 1] == color_to_fill):
                            image[i][j - 1] = color
                            filled += 1
                        if j < (len(image[0]) - 1) and (image[i][j + 1] == color_to_fill):
                            image[i][j + 1] = color
                            filled += 1
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == -1:
                    image[i][j] = color
        return image

