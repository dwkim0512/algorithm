from collections import deque

def solution(progresses, speeds):
    answer = []
    day = deque()
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        day.append(count)
    current = day.popleft()
    result = 1
    while day:
        if day[0] <= current:
            result += 1
            day.popleft()
        else:
            answer.append(result)
            current = day.popleft()
            result = 1
    answer.append(result)
    
    return answer

