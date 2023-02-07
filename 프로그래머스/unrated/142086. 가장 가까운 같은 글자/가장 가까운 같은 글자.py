def solution(s):
    answer = {}
    result = []
    for idx, letter in enumerate(s):
        if letter in answer.keys():
            result.append(idx - answer[letter])
            answer[letter] = idx
        else:
            answer[letter] = idx
            result.append(-1)
    return result