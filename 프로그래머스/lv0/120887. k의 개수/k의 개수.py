def solution(i, j, k):
    
    # for x in range(i,j+1):
    #     for letter in str(x):
    #         if letter == str(k):
    #             answer += 1
    
    return sum(map(lambda x: str(x).count(str(k)), range(i,j+1)))

