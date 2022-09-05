from collections import deque


msg = {"out": "님이 나갔습니다.", "in": "님이 들어왔습니다."}


def solution(record):
    users = {}
    inout_list = deque()

    for row in record:
        temp = list(row.split())
        cmd, user, nick = temp[0], temp[1], temp[2] if len(temp) > 2 else ""

        if cmd == "Change":
            users[user] = nick
        elif cmd == "Enter":
            users[user] = nick
            inout_list.append([user, "in"])
        elif cmd == "Leave":
            inout_list.append([user, "out"])

    return ["".join([users[id], msg[mid]]) for id, mid in inout_list]

