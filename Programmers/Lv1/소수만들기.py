import itertools

def solution(nums):
    answer = 0
    check = 0
    com = list(itertools.combinations(nums, 3))
    
    for i in com:
        s = sum(i)
        check = 0
        for j in range(2, sum(i)):
            if s % j == 0:
                check += 1
        if check == 0:
            answer += 1
    print(answer)
    return answer