def solution(s):
    stack = []
    for c in s: #���ÿ� �� ���ڿ��� �ְ� �������� ���Ͽ� ������ �����ϰ� �ƴϸ� �������� �� (�ݺ�)
        if stack:
            if stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    #�������� ���ÿ� ���ڰ� ������ �������̾������ɷ� �����ϰ� 0����, �ƴϸ� 1����
    if stack: 
        return 0
    else:
        return 1