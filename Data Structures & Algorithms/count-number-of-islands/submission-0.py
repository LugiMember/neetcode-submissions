class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = []
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(rows):
            for col in range(cols):
                curr = grid[row][col]

                if curr == "1" and ((row, col) not in visited):
                    print("THIS RUNS")
                    queue.append((row,col))
                    visited.add((row,col))
                    
                    # do bfs
                    while queue:
                        temp = queue.pop()
                        c_row = temp[0]
                        c_col = temp[1]

                        for dr, dc in directions:
                            nr = c_row + dr
                            nc = c_col + dc

                            # check all directions
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == "1" and (nr, nc) not in visited:
                                    queue.append((nr,nc))
                                    visited.add((nr, nc))
                    islands +=1

        return islands
