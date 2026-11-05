def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            if j == 0:
                land[i][j] += max(land[i-1][1], land[i-1][2], land[i-1][3])
            elif j == 1:
                land[i][j] += max(land[i-1][0], land[i-1][2], land[i-1][3])
            elif j == 2:
                land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][3])
            else:
                land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    return max(land[-1])

'''
자기 자리에 이전 위치 기준 가능한 가장 큰 값을 더해줌
def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[-1])
    '''