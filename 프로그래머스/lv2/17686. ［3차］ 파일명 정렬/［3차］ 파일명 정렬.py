import re
def solution(files):
    answer = []
    for idx, each_file in enumerate(files):
        x = re.findall(r'([a-zA-Z\ \.\-]+)([0-9]+)(.*)', each_file)
        HEAD, BODY, TAIL = map(str, x[0])
        lst_for_order = [HEAD.upper(), int(BODY), idx]
        answer.append(lst_for_order)
        
    answer.sort()
    final = [files[lst_for_order[2]] for lst_for_order in answer]
    
    return final
    
    
