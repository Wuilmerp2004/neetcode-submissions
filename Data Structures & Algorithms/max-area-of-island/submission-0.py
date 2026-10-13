class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0], [0,1],[0,-1]]
        area = 0 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: 
                    grid[r][c] = 0 
                    stack = [[r,c]]
                    size = 0 
                    while stack: 
                        rows, cols = stack.pop()
                        size += 1
                        for dr, dc in directions: 
                            nr, nc = rows + dr, cols + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1: 
                                grid[nr][nc] = 0
                                stack.append((nr,nc))
                    area = max(area, size)
        return area        



        