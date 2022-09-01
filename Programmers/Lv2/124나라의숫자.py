def solution(n):
    answer = ''
    while n:
        if n%3==0: 
            answer = '4' + answer
            n= n//3-1
            continue
        elif n%3==1: answer = '1' + answer
        else: answer = '2' + answer
        n//=3
        
    return answer

'''
3���� �������� ��� ����
�������� ���� ��
0->4 (n-1)
1->1
2->2
'''