def delete_nth(order,max_e):
    order_count = {}
    result = []
    
    for num in order:
        if num not in order_count or order_count[num] < max_e:
            result.append(num)
            
            order_count[num] = order_count.get(num, 0) + 1
        
    return result
            
