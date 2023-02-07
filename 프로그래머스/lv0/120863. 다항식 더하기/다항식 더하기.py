import re

def solution(polynomial):
    polynomial = re.sub("(?<!\d)x", "1x", polynomial)
    # 숫자 다음에 오지 않는 x

    lst = polynomial.split(" + ")
    constant = 0
    x_num = 0

    for each in lst:
        if "x" in each:
            each = each.strip()[:-1]
            x_num += int(each)
        else:
            constant += int(each)

    result = ""
    if constant == 0:
        result += (str(x_num) if x_num !=1 else "") + "x"
    elif x_num == 0:
        result = str(constant)
    else:
        if x_num == 1:
            x_str = ''
        else:
            x_str = str(x_num)
        result = x_str+"x + " + str(constant)
    return result





# def solution(polynomial):
    
#     lst = polynomial.split(' + ')
#     constant = 0
#     x_num = 0
#     for i in lst:
#         if i.isdecimal():
#             constant+=int(i)
#         else:
#             x_num += int(i[:-1]) if i!='x' else 1
#     if constant == 0:
#         return str(x_num) + 'x'
#     elif x_num == 0:
#         return str(constant)
#     elif x_num != 0 and constant !=0:
#         return str(x_num)+ 'x + ' + str(constant)
    