def solution(number, k):
    stack=[]
    for n in number: 
        while k>0 and stack and stack[-1]<n: #k�� 0����ũ��, stack�� ���� �����ϰ� stack���������� n���� ������ �ݺ�
            #while���� ������ �ٲ�� ������
            stack.pop()
            k-=1
        stack.append(n)
    return ''.join(stack[:len(stack)-k]) #����ū ���� ��� ���� ����Ʈ�� join�ؼ� ��ħ


number="4177252841"
k=4
solution(number,k)

'''
for n in number������ �ݺ���ȸ�Ѵ�
stack����Ʈ�� ������
������ ����ٸ� n�� push�ϰ�
���ÿ� ���� ������ n�� ���Ͽ� ������ ������ ����
n���� ������ stack�� pop�ϰ� �ƴ϶�� n�� �ְ� k--�Ѵ�.
�ݺ��� �����Ŀ� k>0�̶�� ���ÿ��� k��ŭ�� �����Ѵ�.
'''