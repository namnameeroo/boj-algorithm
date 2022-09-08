def solution(s):
    answer = ""

    for w in s:
        chunk = ''
        print(w)
        if answer=='' or answer[-1] == ' ': 
            answer += w.upper()
        else:
            answer += w.lower()
    return answer

