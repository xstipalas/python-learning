def better_than_average(class_points, your_points):
    mean_points = (sum(class_points) + your_points) / (len(class_points) + 1)
    
    return your_points > mean_points
