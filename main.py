from MapClass import Map
import random
import heapq
def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                start = (r, c)
            elif grid[r][c] == 3:
                end = (r, c)
    if start is None or end is None:
        return None  

    dist = [[float('inf')] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    
    pq = [(0, start)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while pq:
        current_dist, (r, c) = heapq.heappop(pq)
        if (r, c) == end:
            break  
        
        if current_dist > dist[r][c]:
            continue
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                new_dist = current_dist + 1
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    prev[nr][nc] = (r, c)
                    heapq.heappush(pq, (new_dist, (nr, nc)))
    
    if dist[end[0]][end[1]] == float('inf'):
        return None  # No path found
    
    path = []
    node = end
    while node:
        path.append(node)
        node = prev[node[0]][node[1]]
    path.reverse()
    return path

map = Map(size=51, extra_connection_chance=0.01)
while True:
    map.markShortestPath(dijkstra(map.grid))
    map.printMap()
    input()
    map.regenerate()

