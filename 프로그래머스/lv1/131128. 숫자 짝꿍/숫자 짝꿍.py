from collections import Counter
def solution(X, Y):
    answer = ''
    add =''
    cx = Counter(X)
    cy = Counter(Y)
    for i in sorted(list(set(cx.keys())&set(cy.keys())), reverse=True):
        i = str(i)
        add=i*min(cx[i],cy[i])
        if i=='0' and len(answer) == 0:
            answer += str(int(add))
        else:
            answer += add
    return answer if answer else '-1'

# from collections import Counter
# def solution(X, Y):
#     answer = ''
#     cx = Counter(X)
#     cy = Counter(Y)
#     for i in set(cx.keys())&set(cy.keys()):        
#         answer += str(i)*min(cx[i], cy[i])
        
#     if len(answer)==0: return "-1"
#     answer = sorted(answer, reverse=True)
#     if answer[0]=='0': return '0'
#     return ''.join(answer)