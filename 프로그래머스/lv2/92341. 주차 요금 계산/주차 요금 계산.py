def solution(fees, records):
    answer = []
    default_price, default_time = fees[1],fees[0]
    unit_price, unit_time = fees[3],fees[2]

    
    in_dic = {}

    new_records = [x.split() for x in records]
    car_list = {x[1]:{'hist':[],'acc_time':0} for x in new_records}   # car[nums] = {hist:[], charge:0}
    

    
    for time, num, state in new_records:
        h, m = map(int, time.split(':'))
        time = h*60 + m

        if state =='IN':
            car_list[num]['hist'].append(time)
        if state =='OUT':
            in_time = car_list[num]['hist'].pop()
            car_list[num]['acc_time'] += time-in_time
            
    print(car_list)
    # charging
    result = []
    for num,content in car_list.items():
        # content['acc_time']
        if len(content['hist'])!=0:
            content['acc_time'] += (23*60+59-content['hist'].pop())
            print(content)
        over_time = (content['acc_time']-default_time+unit_time-1)
        over_charge = (over_time//unit_time) if over_time>0 else 0
        tot = over_charge*unit_price + default_price
        print(over_charge)
        print(tot)
        result.append([num, tot])
    result.sort(key=lambda x: (x[0],x[1]))
    return [car[1] for car in result]