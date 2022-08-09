def solution(n, lost, reserve):
    # 1. Set�� �����
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))
    reserve_only.sort();
    
    # 2. ������ �������� �յڸ� Ȯ���Ͽ� ü������ ����ش�.
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)

    #3. �ִ��� ������ �ڿ� lost�� �����ִ� �л����� ü������ ���� �л����̴�.
    return n - len(lost_only)

print(solution(5,[2,4],[1,3,5]))