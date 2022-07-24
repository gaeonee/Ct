def solution(X, Y):
    answer = ''
    equal = ''
    for i in X:
        if i in Y:
            idx = Y.index(i)
            Y = Y[:idx] + Y[idx+1:]
            equal+=i
    if equal == '':
        return "-1"
    answer = int("".join(sorted(equal, reverse = True)))
    return str(answer)
#효율성감점-73.7