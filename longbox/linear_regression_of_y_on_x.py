def regression_line(x: list[int | float], y: list[int | float]):
    n = len(x)
    
    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(x[i] * y[i] for i in range(n))
    x_sq_sum = sum(x_i ** 2 for x_i in x)
    
    a = (x_sq_sum * y_sum - x_sum * xy_sum) / (n * x_sq_sum - x_sum ** 2)
    b = (n * xy_sum - x_sum * y_sum) / (n * x_sq_sum - x_sum ** 2)
    
    return a, b
