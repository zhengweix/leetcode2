class Solution:
    '''
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
    You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
    Return the modified image after performing the flood fill.

    Example 1:
    https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

    Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel is already colored 0, so no changes are made to the image.

    Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 216
    0 <= sr < m
    0 <= sc < n

    Array, Depth-First Search, Breadth-First Search, Matrix

    Island Perimeter, Distribute Candies, Leaf-Similar Trees, Number of Closed Islands
    '''
    def floodFill(self, image, sr, sc, color):
        color1 = image[sr][sc]
        if color1 != color:
            m, n = len(image), len(image[0])
            queue = [(sr, sc)]
            while queue:
                y, x = queue.pop(0)
                image[y][x] = color
                for y1, x1 in (y-1, x), (y, x-1), (y, x+1), (y+1, x):
                    if 0 <= y1 < m and 0<= x1 < n and image[y1][x1] == color1:
                        queue.append((y1, x1))
        return image

    def main(self):
        print(self.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

S = Solution()
S.main()