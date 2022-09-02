from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    half_value = (sum(q1)+sum(q2))//2
    q1_sum = sum(q1)
    while q1 and q2:
        if q1_sum == half_value:
            return answer
        elif q1_sum < half_value:
            q1.append(q2.popleft())
            q1_sum += q1[-1]
            answer += 1
        else:
            q1_sum -= q1.popleft()
            answer += 1
        
    return -1