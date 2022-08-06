def solution(s):
    answer = 111
    length = len(s)
    num_array = []
    for i in range(length):
        if length < 3:
            return -1
        elif length == 3:
            if s[0] == s[1] == s[2]:
                return int(s[0:])
            return -1
            break
        else:
            if i == length - 3:
                if s[i] == s[i+1] == s[i+2]:
                    num_array.append(int(s[i:]))
                break
            if s[i] == s[i+1] == s[i+2]:
                num_array.append(int(s[i:i+3]))
            else:
                continue
    num_array.sort(reverse=True)
    return num_array[0]
'''

'''

s="12223"
solution(s)

s = int(s)
print(s[0:3])