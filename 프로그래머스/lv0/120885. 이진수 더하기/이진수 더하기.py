def solution(bin1, bin2):
    
    result = int(bin1,2) + int(bin2,2)
    answer = bin(result)[2:]
    
    return answer