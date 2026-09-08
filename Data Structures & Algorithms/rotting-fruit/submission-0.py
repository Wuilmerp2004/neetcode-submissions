class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0 
        q = deque()

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    fresh += 1
                elif grid[r][c] == 2: 
                    q.append([r,c])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh > 0: 
            for i in range(len(q)): 
                r, c = q.popleft()
                for dr, dc, in directions: 
                    rows, cols = dr + r, dc + c
                    if (rows < 0 or rows == ROWS or cols < 0 or cols == COLS or grid[rows][cols] != 1): 
                        continue 
                    grid[rows][cols] = 2
                    fresh -= 1
                    q.append([rows,cols])
            time += 1
        return time if fresh == 0 else -1
            


        