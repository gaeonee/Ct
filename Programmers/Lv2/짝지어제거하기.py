def solution(s):
    stack = []
    for c in s: #스택에 한 문자열을 넣고 다음값과 비교하여 같으면 제거하고 아니면 다음값과 비교 (반복)
        if stack:
            if stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    #마지막에 스택에 문자가 있으면 같은값이없었던걸로 간주하고 0리턴, 아니면 1리턴
    if stack: 
        return 0
    else:
        return 1