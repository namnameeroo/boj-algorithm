import sys

input = sys.stdin.readline


def str_to_int(word):
    time = list(map(int, word.split(":")))
    return time[0] * 3600 + time[1] * 60 + time[2]


def int_to_str(time):
    h = str(time // 3600)
    m = str((time % 3600) // 60)
    s = str((time % 3600) % 60)
    return h.zfill(2) + ":" + m.zfill(2) + ":" + s.zfill(2)


def solution(p, ad, logs):
    playtime = str_to_int(p)
    adtime = str_to_int(ad)
    dp = [0] * playtime+[0]
    for l in logs:
        startAt, endAt = map(str_to_int, l.split("-"))
        dp[startAt] += 1
        dp[endAt] -= 1
    
    for i in range(1, playtime):
        dp[i] = dp[i-1]+dp[i]

    for j in range(1, playtime):
        dp[j] = dp[j - 1] + dp[j]

    # max 고르기
    max_people = 0
    timeAt = 0
    for j in range(adtime - 1, playtime):
        people = dp[j] - dp[j - adtime]
        if people > max_people:
            max_people = people
            timeAt = j - adtime + 1
        elif people == max_people:
            if timeAt > j - adtime + 1:
                timeAt = j - adtime + 1

    return int_to_str(timeAt)
