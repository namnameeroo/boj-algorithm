def solution(rsp):
    # 가위 2, 바위 0, 보 5
    board = {'2':'0','0':'5','5':'2'}
    return ''.join([board[x] for x in rsp])