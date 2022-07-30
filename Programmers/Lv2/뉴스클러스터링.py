import math
def solution(str1, str2):
    str1_list=[]
    str2_list=[]
    str1 = str1.upper()
    str2 = str2.upper()
    
    #특수문자가 있는경우 글자쌍을 버리기 때문에 아래 코드는 틀림
    #str1 = re.sub('[^a-zA-Z]','',str1.upper()) 
    #str2 = re.sub('[^a-zA-Z]','',str2.upper())  #str1, str2에서 영문자만 남기고 제거함

    for i in range(len(str1)-1): #str1와 str2 문자열의 글자쌍이 영어일경우 해당 글자쌍을 새 리스트에 저장함
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i]+str1[i+1])
            
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i]+str2[i+1])
    
    intersection = set(str1_list) & set(str2_list)
    union = set(str1_list) | set(str2_list)

    if len(union) == 0:
        return 65536
    
    intersection_len = sum([min(str1_list.count(inter), str2_list.count(inter)) for inter in intersection])
    union_len = sum([max(str1_list.count(u), str2_list.count(u)) for u in union])
    
    return math.trunc((intersection_len/union_len)*65536)