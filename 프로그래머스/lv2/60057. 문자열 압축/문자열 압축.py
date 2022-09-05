def solution(word):
    answer = 10**3
    for unit in range(1, (len(word) // 2 )+ 2):
        prev_unit = word[0:unit]
        count = 1
        result = ""

        for i in range(unit, len(word)+1, unit):
            curr = word[i : i + unit]

            if prev_unit == curr:
                count += 1

            else:
                result += str(count) + prev_unit if count > 1 else prev_unit
                prev_unit = curr
                count = 1

        result += str(count) + prev_unit if count > 1 else prev_unit
        answer = min(len(result), answer)
    return answer
