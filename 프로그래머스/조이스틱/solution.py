def solution(name):
    dict_count = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
        'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
        'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
        'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
        'Y': 24, 'Z': 25
    }
    
    answer = 0
    len_alphabet = len(dict_count)
    len_name = len(name)
    move = len(name) - 1

    for c in name:
        if dict_count[c] <= len_alphabet//2:
            answer += dict_count[c]
        else:
            answer += len_alphabet - dict_count[c]

    for i in range(len(name)):
        next = i + 1

        while next < len(name) and name[next] == 'A':
            next += 1

        move = min(
            move,
            i * 2 + len(name) - next,
            i + (len(name) - next) * 2
        )
    answer += move
    
    return answer