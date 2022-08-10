'''
https://leetcode.com/problems/number-of-islands/

Solution:
__________
Use DFS, that's it. For each 1s, look for all the adjacent 1s in the 4 directions.
'''

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialize a map of False values - which means none of the items are visited
        mapOfVisits = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        
        def markNeighbors(i, j, mapOfVisits, grid):
            if (i < 0) or (j > len(grid[0])-1) or (j < 0) or (i > len(grid)-1) or (grid[i][j] == "0")  or mapOfVisits[i][j]:
                return
            mapOfVisits[i][j] = True
            markNeighbors(i+1, j, mapOfVisits, grid)
            markNeighbors(i, j+1, mapOfVisits, grid)
            markNeighbors(i-1, j, mapOfVisits, grid)
            markNeighbors(i, j-1, mapOfVisits, grid)
        
        isLand = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # Run a loop for each 1s found in case it's not visited already
                if (grid[i][j]== '1') and not mapOfVisits[i][j]:
                    markNeighbors(i, j, mapOfVisits, grid)
                    isLand += 1
        return isLand
   
