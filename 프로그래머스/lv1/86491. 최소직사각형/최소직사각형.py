def solution(sizes):
    
    w = [min(x) for x in sizes]
    h = [max(x) for x in sizes]
    answer = max(w)*max(h)

    return answer

# def solution(sizes):
#     sizes = [sorted(x) for x in sizes]
    
#     w = 0
#     h = 0
#     for x in sizes:
#         w = max(w, x[0])
#         h = max(h, x[1])
#     answer = w*h

#     return answer