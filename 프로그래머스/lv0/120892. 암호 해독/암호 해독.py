def solution(cipher, code):
    answer = ''
    
    for idx in range(len(cipher)):
        if (idx + 1) % code == 0:
            answer += cipher[idx]
    
    return answer