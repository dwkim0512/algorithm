def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)

    if total % 2 != 0:
        return -1

    target = total // 2

    queue3 = (queue1 + queue2) * 2

    count = 0
    left = 0
    right = len(queue1)

    current_sum = sum(queue1)

    n = len(queue1)

    while count <= 3 * n:
        if current_sum == target:
            return count

        if current_sum < target:
            if right >= len(queue3):
                break
            current_sum += queue3[right]
            right += 1

        else:
            current_sum -= queue3[left]
            left += 1

        count += 1

    return -1

'''
큐 두개를 붙여서 포인터를 달아놓으면 포인터의 이동이 큐의 이동이 된다
[3, 2, 7, 2, 4, 6, 5, 1]에 각각 큐의 앞부분인 3, 4에 포인터를 달고 움직이면 left-right 사이에 있는 합들이 각 큐의 합이 되는 것
'''