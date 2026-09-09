class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        island = 0

        def bfs(r, c): 
            q = deque()
            grid[r][c] = '0'
            q.append((r,c))
            while q: 
                rows , cols = q.popleft() 
                for dr, dc in directions: 
                    nr, nc = dr + rows , dc + cols
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0'): 
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = '0'
                        
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == '1':
                    bfs(r,c)
                    island += 1
                        
                    
        return island

            
            
        