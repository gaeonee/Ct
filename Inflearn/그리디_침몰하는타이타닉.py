import sys
#sys.stdin=open("input.txt", "rt")


#[list(map(int,input().split())) for _ in range(n)]
#p =  [list(input().strip()) for _ in range(n)]
#def overlap_delete(s):

#def solution(s):

N, M = map(int, input().split())
cnt = 0
ship = list(map(int, input().split())) #현재 보트 탑승객 무게
ship.sort() #오름차순 정렬시 첫번째값은 제일 작고 마지막 값은 가장 큰값


while ship:
    if len(ship) == 1:
        cnt += 1
        break
    if ship[0] + ship[-1] > M:
        ship.pop() #제일 큰 마지막 항목을 pop함
        cnt += 1
    else:
        ship.pop(0)
        ship.pop()
        cnt += 1
print(cnt)