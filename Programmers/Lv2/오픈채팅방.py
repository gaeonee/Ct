def solution(record):
    answer = []
    size=len(record)
    record_split=[list(map(str, i.split())) for i in record]
    dic={}

    for i in range(size):
        if record_split[i][0]in ["Enter", "Change"]:
            dic[record_split[i][1]]=record_split[i][2]

    for j in range(size):
        if record_split[j][0]=="Enter":
            answer.append(dic[record_split[j][1]]+"님이 들어왔습니다.")
        elif record_split[j][0]=="Leave":
            answer.append(dic[record_split[j][1]]+"님이 나갔습니다.")

    return answer