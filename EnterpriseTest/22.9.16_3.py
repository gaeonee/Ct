def solution(n):
    answer = 0
    cnt = 0
    while n <= 100:
        n = list(str(n)) #['1','9']
        for i in n:
            answer += int(i)*int(i)

        cnt += 1
        n = answer
        answer = 0
        if n == 1:
            return cnt

    return -1