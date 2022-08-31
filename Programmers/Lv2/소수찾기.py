import itertools

def prime_check(value):
    if value < 2:
        return False
    for i in range(2, value//2+1):

        if value%i == 0:
            return False
        
    return True

def solution(numbers):
    cnt=0
    permutation_list=[]
    result=[]
    for i in range(1,len(numbers)+1):
        permutation_list.extend(itertools.permutations(numbers,i))
        result=[int(''.join(i))for i in permutation_list]
    permutation_list=list(set(permutation_list))
    for j in set(result):
        if prime_check(j) == True:
            cnt+=1
    return cnt
'''
1. �ݺ����� itertools.permutations�� ���հ����� ������ ��� ã�� ����Ʈ�� extends�� ����
2.�ش� ����Ʈ�� ''.join���� ���� Ʃ���� ������ ������ ������
3.set���� ����Ʈ�� �ߺ�����
4.for������ �Ҽ��� ã�� �Լ��� ���� ��ȯ���� true�̸� cnt�� ������
5.�ݺ����� ������ cnt�� ��ȯ��
'''