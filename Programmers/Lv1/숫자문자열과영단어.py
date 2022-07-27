def solution(s):
    answer = 0
    start=-1
    num_dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for i in range(len(s)):
        if not s[i].isdigit():
            if s[start+1:i+1] in num_dic:
                answer = answer*10 + num_dic[s[start+1:i+1]]
                start=i
        else:
            answer = answer*10 + int(s[i])
            start=i

    return answer
'''
해당 코드보다 아래코드처럼
.replace(기존,변경문자)로하면 훨씬 효율적임

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
'''

s="one4seveneight"
solution(s)