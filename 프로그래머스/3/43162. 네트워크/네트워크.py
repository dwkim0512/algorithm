def solution(n, computers):
    visited = [False] * n
    
    answer = 0
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == False:
                dfs(j)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer