from itertools import combinations
def solution(number):
    answer = 0
    combi = combinations(number,3)
    for i in combi:
        if sum(i) == 0:
            answer += 1
    return answer