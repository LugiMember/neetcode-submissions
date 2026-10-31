from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_orange = 0
        minute = 0

        rows = len(grid)
        cols = len(grid[0])

        # so find the starting rotten
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.appendleft((r,c))
                elif grid[r][c] == 1:
                    fresh_orange += 1

        # EDGE CASE: No fresh oranges means 0 minutes needed
        if fresh_orange == 0:
            return 0


        # STEP 2: Define directions instead of writing 4 separate checks
        # (row change, column change)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # STEP 3: BFS - process one level (minute) at a time
        while queue:
            
            for _ in range(len(queue)):
                r, c = queue.popleft()

                #check all 4 directions
                for dr, dc, in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:

                        # Only spread to fresh oranges
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2  # Mark visited immediately
                            fresh_orange -= 1

                            # Newly rotten oranges spread NEXT minute
                            queue.append((nr, nc))


            # Only count a minute if fresh oranges remain
            # or if this round just rotted the final fresh orange
            if queue:
                minute += 1

        # STEP 4: Check whether every fresh orange was reached
        if fresh_orange > 0:
            return -1

        return minute

