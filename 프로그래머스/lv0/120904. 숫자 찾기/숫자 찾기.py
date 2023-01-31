def solution(num, k):
    answer = -1
    k = str(k)
    for i, v in enumerate(list(str(num))):
        if v == k:
            answer = i + 1
            break
    
    return answer