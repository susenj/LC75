'''
Note: Copied from LeetCode solution as I couldn't do it by myself
https://leetcode.com/problems/flood-fill/
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the 
pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the
same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Solution:
_________

BFS approach: 

'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        R, C = len(image), len(image[0])
        curr_color = image[sr][sc]
        if curr_color == color: return image # Return becuase if the new color is same as the color of the pixel, there is no point of changing it.
        def bfs(r, c):
            if image[r][c] == curr_color:
                image[r][c] = color
                if r >= 1: bfs(r-1, c)
                if r+1 < R: bfs(r+1, c)
                if c >= 1: bfs(r, c-1)
                if c+1 < C: bfs(r, c+1)

        bfs(sr, sc)
        return image
