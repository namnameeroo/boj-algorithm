
def solution(n, lost, reserve):
    # n 학생수, lost 도난당한 애들 배열, reserve 여벌 배열
    # 체육 몇명이서 들을 수 있니, 단 대여는 앞뒤로만 가능
    answer = 0
    borr = 0

    new_lost = sorted([x for x in lost if x not in reserve])
    new_reserve = sorted([y for y in reserve if y not in lost])
    print(new_lost)

    for i in new_lost :
        check = False
        for j in [-1,0,1]:
            if i+j in new_reserve and not check :
                check = True
                new_reserve[new_reserve.index(i+j)] = 0
                borr += 1
                break
            
            
    # reserve 여분 애들 => 노상관
    # len(lost) - borr => 아직 못빌린 애들
    answer = n - len(new_lost) + borr
    print(answer)
    return answer