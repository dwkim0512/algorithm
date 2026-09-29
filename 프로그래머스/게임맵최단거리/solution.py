from collections import deque
def solution(maps):
    queue = deque()
    queue.append((0,0))
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    n = len(maps)
    m = len(maps[0])

    distance = [[0] * m for _ in range(n)]
    distance[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and distance[nx][ny] == 0:
                queue.append((nx,ny))
                distance[nx][ny] = distance[x][y] + 1
            
    return -1 if distance[n-1][m-1] == 0 else distance[n-1][m-1]