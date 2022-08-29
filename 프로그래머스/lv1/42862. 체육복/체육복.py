def solution(n, lost, reserve):
    lost = set(lost)
    num_lost = len(lost)
    reserved = set(reserve) - set(lost)
    losted = set(lost) - set(reserve)

    for r in sorted(reserved):
        if r - 1 in losted:
            losted = losted - {r - 1}

        elif r + 1 in losted:
            losted = losted - {r + 1}

    return n - len(losted)
