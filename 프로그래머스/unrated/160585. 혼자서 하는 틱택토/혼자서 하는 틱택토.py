def solution(board):
    def checkOverCase(cnt_o, cnt_x):
        starter_win = 0
        follower_win = 0
        for i in range(3):
            if board[i] == "OOO":
                starter_win += 1
            if board[i] == "XXX":
                follower_win += 1

            col = board[0][i] + board[1][i] + board[2][i]
            if col == "OOO":
                starter_win += 1
            if col == "XXX":
                follower_win += 1

        cross1 = board[0][0] + board[1][1] + board[2][2]
        cross2 = board[0][2] + board[1][1] + board[2][0]
        if cross1 == "OOO" or cross2 == "OOO":
            starter_win += 1
        if cross1 == "XXX" or cross2 == "XXX":
            follower_win += 1
        print(starter_win, follower_win)

        if starter_win > follower_win:
            if count_o > count_x:
                return True
            else:
                return False
        elif follower_win > starter_win:
            if count_x == count_o:
                return True
            else:
                return False
        else:
            if starter_win == 0:
                return True
            else:
                return False

        return False

    combined = "".join(board)
    count_o = combined.count("O")
    count_x = combined.count("X")
    if count_o == count_x or count_o == count_x + 1:
        if count_o >= 3 and count_x >= 3 and not checkOverCase(count_o, count_x):
            return 0
        return 1
    else:
        return 0