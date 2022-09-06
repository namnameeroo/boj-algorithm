def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    answer = ''
    for s in new_id:
        if s.isdecimal() or s.isalpha() or (s in ['-','_','.']):
            # 3
            if not(len(answer) > 0 and answer[-1] == '.' and s =='.'):
                answer += s

    #4
    if len(answer) > 1:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    if answer=='' or answer=='.' :
        answer = 'aaa'
    if len(answer)>15: 
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) < 3:
        answer+=answer[-1]*(3-len(answer))

    # print(answer)
    return answer