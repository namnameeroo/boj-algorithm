def solution(emergency):
    answer = []
    sorted_e = sorted(emergency, reverse=True)
    dic = {patient:order for order, patient in enumerate(sorted_e)}

    for patient in emergency:
        answer.append(dic[patient]+1)
        
    return answer