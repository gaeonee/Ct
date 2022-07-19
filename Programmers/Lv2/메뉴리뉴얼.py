from itertools import combinations

def solution(orders, course):
    answer = []
    order_combinations = [] #orders배열의 중복없는 조합을 저장할 리스트
    order_dict = {} #추출된 조합을 저장할 딕셔너리

    for c in course: #코스[2,3,4]대로 순차적으로 orders 조합을 추출해 저장함
        for order in orders:
            order_combinations.extend(list(map(''.join, combinations(order,c)))) # append대신 extends를 씀으로써 [[1,2],1,2]처럼 저장되지 않고 []내부의 '[]'부호를 제거하여 저장함

        for order_combination in order_combinations: #조합을 순차탐색하면서 해당 조합이 딕셔너리에 있으면 1을 추가하고 아니면 딕셔너리에 추가
            if order_combination in order_dict:
                order_dict[order_combination]+=1
            else:
                order_dict[order_combination]=1
        for order in order_dict:
           if order_dict[order] == max([order_dict[order] for order in order_dict]):
               if order_dict[order]>1:
                   answer.append(order)
                   

    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
solution(orders,course)