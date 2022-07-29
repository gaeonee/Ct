import re
import math
def solution(str1, str2):
    answer = 0
    str1_list=[]
    str2_list=[]
    str1 = re.sub('[^a-zA-Z]','',str1.upper()) 
    str2 = re.sub('[^a-zA-Z]','',str2.upper())  #str1, str2에서 영문자만 남기고 제거함
    if not str1 and not str2:
        return 1 * 65536
    else:
        for i in range(len(str1)-1):
            str1_list.append(str1[i]+str1[i+1])
        for i in range(len(str2)-1):
            str2_list.append(str2[i]+str2[i+1])
    
    print(str1_list, str2_list)
    intersection = list(set(str1_list) & set(str2_list))
    union = list(set(str1_list) | set(str2_list))
    
    
    return math.trunc((len(intersection)/len(union))*65536)