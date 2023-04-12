def solution(name, yearning, photo):
    
#     dic = {name[idx]:yearning[idx] for idx in range(len(name))}
#     answer = [sum([dic[r] for r in row if r in name]) for row in photo]

    return [sum(yearning[name.index(r)] for r in row if r in name) for row in photo]
    