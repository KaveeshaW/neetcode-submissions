class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visited = set()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count += 1
                    q.append((r, c))
                    visited.add((r, c))
                    self.bfs(grid, q, visited)
        return count

    def bfs(self, grid, q, visited):
        while q:
            (check_r, check_c) = q.popleft()
            for dr, dc in self.neighbors(grid, check_r, check_c):
                if grid[dr][dc] == '1' and (dr, dc) not in visited:
                    q.append((dr, dc))
                    visited.add((dr, dc))

    def neighbors(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = []
        for dr, dc in directions:
            nr = dr + row
            nc = dc + col
            if 0 <= nr < rows and 0 <= nc < cols:
                res.append((nr, nc))
        return res




