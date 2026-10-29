from collections import deque

def solution(maps):
    m = len(maps[0])
    n = len(maps)
    visited = [[False] * m for _ in range(n)]
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
