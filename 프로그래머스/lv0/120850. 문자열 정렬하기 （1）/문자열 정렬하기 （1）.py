def solution(my_string):
    filtered = [int(x) for x in my_string if x.isdecimal()]
    filtered.sort()
    return filtered




# import re
# def solution(my_string):
#     return re.sub('[aeiou]', '', my_string)