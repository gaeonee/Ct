def pairTest(u): #�ùٸ� ��ȣ ���ڿ� Ȯ��
    stack = []
    for i in u:
        if i == '(': #'('������ ���ÿ� �߰�
            stack.append(i)
        else: #')'������ ������ ������ ����pop
            if not stack: #������ ������� ��� ¦�� �����ʱ⶧���� False�� ����
                return False
            stack.pop()

    return True

def solution(p):
    
    def bracket(p):
        a = ''
        open_bracket, close_bracket = 0, 0
        
        if not p:
            return ''

        for i in range(len(p)):
            if p[i]=='(':
                open_bracket += 1
            else:
                close_bracket += 1
            if open_bracket == close_bracket:
                u = p[:i+1]
                v = p[i+1:]
                break

        if pairTest(u): #�ùٸ� ���ڿ��̸�
            return u + bracket(v)
        else: #�ùٸ��� ������
            return '(' + bracket(v) + ')'+"".join(list(map(lambda x : '(' if x==')' else ')',list(u[1:-1]))))

    return bracket(p)
'''
'''

p="()))((()"
solution(p)