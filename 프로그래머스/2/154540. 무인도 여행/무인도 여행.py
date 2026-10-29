from collections import deque

def solution(maps):
    m = len(maps[0])
    n = len(maps)
    visited = [[False] * m for _ in range(n)]
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]    

    for i in range(n):
        for j in range(m):
            # 지도 중 X가 아닌 구역에 대해 bfs 실행
            if maps[i][j] != 'X' and not visited[i][j]:
                sum_zone = int(maps[i][j])
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                            queue.append((nx,ny))
                            visited[nx][ny] = True
                            sum_zone += int(maps[nx][ny])
                answer.append(sum_zone)
                
    return sorted(answer) if answer else [-1]