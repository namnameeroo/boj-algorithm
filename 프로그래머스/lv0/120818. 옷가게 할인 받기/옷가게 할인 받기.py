def solution(price):
    sales = {500000:0.8, 300000:0.9, 100000:0.95, 10: 1}
    price = int(price)
    for standard_price, percentage in sales.items():

        if price >= standard_price:
            return int(price*percentage)
            
    
        
        

    