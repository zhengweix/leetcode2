class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        lr, lc = len(image), len(image[0])
        sources = [[sr, sc]]
        visited = []
        while sources:
            r, c = sources.pop(0)
            visited.append([r, c])
            oldColor = image[r][c]
            image[r][c] = newColor
            if r > 0 and image[r-1][c] == oldColor and [r-1, c] not in visited:
                sources.append([r-1, c])

            if r < lr-1 and image[r+1][c] == oldColor and [r+1, c] not in visited:
                    sources.append([r+1, c])

            if c > 0 and image[r][c-1] == oldColor and [r, c-1] not in visited:
                sources.append([r, c-1])

            if c < lc-1 and image[r][c+1] == oldColor and [r, c+1] not in visited:
                sources.append([r, c+1])

        return image
