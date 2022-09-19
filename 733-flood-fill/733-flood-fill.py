class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def fillPixel(image: List[List[int]], m: int, n: int, sr: int, sc: int, original: int, color: int) -> None:
            if sr < 0 or sr >= m or sc < 0 or sc >= n:
                return
            if image[sr][sc] != original:
                return
            image[sr][sc] = color
            fillPixel(image, m, n, sr + 1, sc, original, color)
            fillPixel(image, m, n, sr - 1, sc, original, color)
            fillPixel(image, m, n, sr, sc + 1, original, color)
            fillPixel(image, m, n, sr, sc - 1, original, color)
        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        if image[sr][sc] != color:
            fillPixel(image, m, n, sr, sc, original, color)
        return image