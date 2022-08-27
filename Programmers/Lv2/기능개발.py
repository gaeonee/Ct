import math
def solution(progresses, speeds):
    temp = list(map(lambda x:100-x,progresses)) 
    remainingDay = list(map(lambda x:(math.ceil(temp[x]/speeds[x])),range(len(progresses)))) #(100-progresses)//speeds�� �ϰ� ���� �ø���
    #remainingDay�� �����ϼ��� ����� �ʱ�ȭ��
    cnt=0
    answer=[]
    first=remainingDay[0]

    while remainingDay: 
        #�����ϼ��� �°� ����(������)���ϰ� remainingDay����Ʈ�� ��� ���ŵɶ����� �ݺ�
        if first>=remainingDay[0]: #ù������ ��ū���̳��ö����� ���������ϰ� cnt+1
            del remainingDay[0]
            cnt+=1
        else: #ù������ ��ū���̳����� ù���� ū�����κ���, answer����Ʈ��cnt�߰��� cnt��0���κ���
            answer.append(cnt)
            first=remainingDay[0]
            cnt=0
    answer.append(cnt)
    return answer