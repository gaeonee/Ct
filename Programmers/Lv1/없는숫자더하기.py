def solution(numbers):
    answer = 0
    num = [i for i in range(10)]
    for n in num:
        if n not in numbers:
            answer+=n
    return answer