from collections import Counter
def solution(X, Y):
    answer = ''
    cx = Counter(X)
    cy = Counter(Y)
    for i in set(cx.keys())&set(cy.keys()):        
        answer += str(i)*min(cx[i], cy[i])
    if len(answer)==0: return "-1"
    answer = sorted(answer, reverse=True)
    if answer[0]=='0': return '0'
    return ''.join(answer)