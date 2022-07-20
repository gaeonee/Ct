def solution(t,p,n):
    answer = 0
    profit = 0
    visit = [True for i in range(n)]
    while False in visit:
        for day in range(n):
            if visit[day]== True:
                continue
            else:
                if day + t[day]-1 >= n:
                    break
                profit += p[day]
                day += t[day]-1
                

    return answer