def solution(dirs):
    x, y = 0, 0
    visited = set()

    for d in dirs:
        if d == 'U':
            nx, ny = x, y + 1
        elif d == 'D':
            nx, ny = x, y - 1
        elif d == 'L':
            nx, ny = x - 1, y
        elif d == 'R':
            nx, ny = x + 1, y

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        visited.add(((x, y), (nx, ny)))
        visited.add(((nx, ny), (x, y)))

        x, y = nx, ny

    return len(visited) // 2