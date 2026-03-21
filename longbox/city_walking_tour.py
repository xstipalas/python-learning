class Group:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
def transfer_time(time: str):
    hours, minutes = (int(num) for num in time.split(':'))
    
    return hours * 60 + minutes
        
def distance_between(obj1, obj2):
    return ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
    
def is_possible_to_visit_all(attractions, hotel_coords, start_time_str, close_time_str):
    cur_time = transfer_time(start_time_str)
    end_time = transfer_time(close_time_str)
    
    tourists = Group(hotel_coords.x, hotel_coords.y, 5)
    
    while attractions:
        cur_attraction = min(attractions, key=lambda attraction: distance_between(tourists, attraction))
        cur_distance = distance_between(tourists, cur_attraction)
                
        cur_time += (cur_distance / tourists.s) * 60 + cur_attraction.v
        
        if cur_time <= end_time:
            attractions.remove(cur_attraction)
            
            tourists.x, tourists.y = cur_attraction.x, cur_attraction.y
        else:
            return False
        
    distance_to_hotel = distance_between(tourists, hotel_coords)
    cur_time += (distance_to_hotel / tourists.s) * 60
    
    return cur_time <= end_time
