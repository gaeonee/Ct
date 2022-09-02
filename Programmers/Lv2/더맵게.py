import heapq
def solution(scoville,k):
    heapq.heapify(scoville)
    answer=0
    while scoville[0]<k: #Ʈ�� ��Ʈ�� ��ġ�� 0�ε����� �׻� ����������
        #scoville�� ���� �������� k���� Ŀ�������� �ݺ�
        if len(scoville)<=1:
            answer=-1
            break
        else:
            heapq.heappush(scoville,(heapq.heappop(scoville)+(heapq.heappop(scoville)*2)))
            #scoville����Ʈ�� �������� �ΰ��� ���� ���� ���� �߰�
            answer+=1
    return answer