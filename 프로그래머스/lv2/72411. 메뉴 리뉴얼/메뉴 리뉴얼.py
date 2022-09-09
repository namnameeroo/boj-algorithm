from itertools import combinations


def solution(orders, course):
    comb_dic = {long: {} for long in course}
    selected = set()

    for long in course:
        best_num = 2
        for guest in orders:
            comb = list(map(sorted, combinations(guest, long)))
            comb = ["".join(arr) for arr in comb if len(arr) > 0]

            for e in comb:
                if not e:
                    continue
                key = "".join(sorted(e))
                if key in comb_dic[long].keys():
                    comb_dic[long][key] += 1
                    best_num = max(best_num, comb_dic[long][key])
                else:
                    comb_dic[long][key] = 1

        for k, v in comb_dic[long].items():
            if v >= best_num:
                selected.add(k)

    selected = sorted(list(selected))
    return selected
