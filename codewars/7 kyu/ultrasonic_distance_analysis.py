def sensor_analysis(sensor_data: list[tuple]) -> tuple[float, float]:
    data = [x[1] for x in sensor_data]
    
    mean = sum(data) / len(data)
    sd = (sum((x - mean) ** 2 for x in data)  / (len(data) - 1)) ** 0.5 
    
    return (round(mean, 4), round(sd, 4))