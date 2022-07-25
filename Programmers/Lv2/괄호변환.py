def pairTest(u): #올바른 괄호 문자열 확인
    stack = []
    for i in u:
        if i == '(': #'('나오면 스택에 추가
            stack.append(i)
        else: #')'나오면 스택의 마지막 값을pop
            if not stack: #스택이 비어있을 경우 짝이 맞지않기때문에 False를 리턴
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

        if pairTest(u): #올바른 문자열이면
            return u + bracket(v)
        else: #올바르지 않으면
            return '(' + bracket(v) + ')'+"".join(list(map(lambda x : '(' if x==')' else ')',list(u[1:-1]))))

    return bracket(p)
'''
'''

p="()))((()"
solution(p)