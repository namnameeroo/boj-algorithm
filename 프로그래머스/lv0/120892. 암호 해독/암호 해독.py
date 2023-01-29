def solution(cipher, code):
    return cipher[code-1::code]
    
    
# 풀이 1    
    # for idx in range(len(cipher)):
    #     if (idx + 1) % code == 0:
    #         answer += cipher[idx]
    
    
# 풀이 2

    # answer = ''.join([cipher[x] for x in range(len(cipher)) if (x+1)%code == 0])    
