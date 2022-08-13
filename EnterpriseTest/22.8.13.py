def solution(A):
    # write your code in Python 3.6
    cnt = 0
    bulb = [False for _ in range(len(A))]
    for i in A:
        bulb[i-1] = True
        if False in bulb[:i]:
            continue
        else: cnt += 1
    return cnt