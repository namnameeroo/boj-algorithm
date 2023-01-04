def solution(angle):
    answer = 0
    if angle >= 180:
        answer += 1
    if angle > 90:
        answer += 1
    if angle >= 90:
        answer += 1
    if angle > 0:
        answer += 1
        
    return answer