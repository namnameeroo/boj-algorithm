import re
def solution(files):
    answer = []
    heads = []
    for idx, each_file in enumerate(files):
        # exacted = ''.join([x for x in each_file if x.isdecimal()])
        
        x = re.findall(r'([a-zA-Z\ \.\-]+)([0-9]+)(.*)', each_file)
        HEAD, BODY, TAIL = map(str, x[0])
        answer.append([HEAD.upper(), int(BODY), idx])        
        
    answer.sort()
    final = []
    for i in answer:
        idx = i[2]
        final.append(files[idx])
    return final
    # return [x[3] for x in answer]
    
    