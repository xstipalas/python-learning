def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    
    a, b, c = signature
    
    for i in range(3, n):
        a, b, c = b, c, a + b + c
        
        signature.append(c)
        
    return signature
    
