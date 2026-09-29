from collections import deque
def solution(begin, target, words):
    queue = deque()
    queue.append((begin,0))
    
    used = []
    used.append(begin)
    while queue:
        word, distance = queue.popleft()
        for i in range(len(words)):
            count = 0
            for j, s in enumerate(words[i]):
                if s == word[j]:
                    count += 1
            if count == len(words[i])-1 and words[i] not in used:
                if words[i] == target:
                    return distance + 1
                else:
                    queue.append((words[i], distance + 1))
                    used.append(words[i])
                
            
    return 0