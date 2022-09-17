def solution(strs):
    length = len(strs[0])
    list_len = len(strs)
    idx = 0
    tmp = ""
    while idx<length:
        if length == 1: #각 문자길이가 1인경우
            tmp = strs[0][0]
            for i in range(1,list_len):
                if tmp != strs[i][0]:
                    return ""
            return tmp

        tmp = strs[0][:idx]
        for i in range(1,list_len):
            if tmp != strs[i][:idx]:
                if len(tmp) ==1:
                    return ""
                return strs[0][:idx-1]
        idx += 1