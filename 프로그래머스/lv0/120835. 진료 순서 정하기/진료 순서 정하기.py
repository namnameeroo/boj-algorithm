def solution(emergency):
    answer = []
    for idx, value in enumerate(emergency):
        answer.append([idx, value])
    answer.sort(key=lambda x : (x[1]), reverse=True)
    result = [0] * len(emergency)
    for i in range(len(emergency)):
        idx = answer[i][0]
        result[idx] = i+1
    return result