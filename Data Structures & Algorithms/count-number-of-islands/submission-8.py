class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == '1': 
                    islands += 1
                    grid[r][c] = '0'
                    stack = [[r,c]]
                    while stack: 
                        r,c = stack.pop()
                        for dr, dc in directions: 
                            rows, cols = dr + r, dc + c
                            if (rows < 0 or cols < 0 or rows == ROWS or cols == COLS or grid[rows][cols] != '1'):
                                continue
                            grid[rows][cols] = '0'
                            stack.append([rows, cols])
        return islands



            
            
        