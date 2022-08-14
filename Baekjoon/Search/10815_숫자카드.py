N = int(input())
n = set(map(int, input().split()))
print(n)
M = int(input())
M_list = list(map(int, input().split()))

card.sort()

def BinarySearch(card, target, start, end,):
    while(start <= end):
        mid = (start + end) // 2

        if(card[mid] == target):
            return True
        elif(card[mid] > target):
            end = mid - 1
        else:
            start = mid + 1

    return False

for i in M_list:
    if BinarySearch(card, i, 0, N-1):
        print(1, end = ' ')
    else: print(0, end = ' ')