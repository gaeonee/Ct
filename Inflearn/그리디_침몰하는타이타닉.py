import sys
#sys.stdin=open("input.txt", "rt")


#[list(map(int,input().split())) for _ in range(n)]
#p =  [list(input().strip()) for _ in range(n)]
#def overlap_delete(s):

#def solution(s):

N, M = map(int, input().split())
cnt = 0
ship = list(map(int, input().split())) #���� ��Ʈ ž�°� ����
ship.sort() #�������� ���Ľ� ù��°���� ���� �۰� ������ ���� ���� ū��


while ship:
    if len(ship) == 1:
        cnt += 1
        break
    if ship[0] + ship[-1] > M:
        ship.pop() #���� ū ������ �׸��� pop��
        cnt += 1
    else:
        ship.pop(0)
        ship.pop()
        cnt += 1
print(cnt)