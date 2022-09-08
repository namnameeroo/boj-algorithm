def solution(record):

    msg = {'Leave':'님이 나갔습니다.', 'Enter':'님이 들어왔습니다.'}
    record = [line.split() for line in record]
    users_dic = {}
    result = []
    for line in record:
        cmd = line[0]
        user = line[1]
        if len(line) == 3:
            users_dic[user] = line[2]
        if line[0] in msg.keys():
            result.append([cmd, user])
    
    txt_list = []
    
    for do in result:
        cmd = do[0]
        userid = do[1]
        txt_list.append(''.join([users_dic[userid],msg[cmd]]))
        

    return txt_list