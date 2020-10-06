class Solution:
    def floodFill(self, image, sr, sc, newColor):
        prevColor = image[sr][sc]

        if (prevColor != newColor):
            self.floodFillUtil(image, sr, sc, prevColor, newColor)

        return image

    def floodFillUtil(self, image, sr, sc, prevColor, newColor):

        R = len(image)
        C = len(image[0])

        if (sr >= 0 and sr < R and sc >= 0 and sc < C and image[sr][sc] == prevColor):
            image[sr][sc] = newColor
            self.floodFillUtil(image, sr + 1, sc, prevColor, newColor)
            self.floodFillUtil(image, sr - 1, sc, prevColor, newColor)
            self.floodFillUtil(image, sr, sc + 1, prevColor, newColor)
            self.floodFillUtil(image, sr, sc - 1, prevColor, newColor)




