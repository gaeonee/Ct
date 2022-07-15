def solution(number, k):
    stack=[]
    for n in number: 
        while k>0 and stack and stack[-1]<n: #k가 0보다크고, stack이 값이 존재하고 stack마지막값이 n보다 작으면 반복
            #while조건 순서가 바뀌면 오류남
            stack.pop()
            k-=1
        stack.append(n)
    return ''.join(stack[:len(stack)-k]) #제일큰 수가 담긴 스택 리스트를 join해서 합침


number="4177252841"
k=4
solution(number,k)

'''
for n in number과같이 반복순회한다
stack리스트를 생성함
스택이 비었다면 n을 push하고
스택에 값이 있으면 n과 비교하여 스택의 마지막 값이
n보다 작으면 stack을 pop하고 아니라면 n을 넣고 k--한다.
반복이 끝난후에 k>0이라면 스택에서 k만큼을 제거한다.
'''