import math

def sum(m, n):
    result = m
    increment = 1 if is_positive(n) else -1

    for i in range(0, n, increment):
        result += increment

    return result

 
def divide(m, n):
    sign = 1
    if not is_positive(m):
        sign *= -1
        m *= -1
    if not is_positive(n):
        sign *= -1
        n *= -1

    result = 0
    while (m >= n and m > 0):
        result += 1
        m -= n

    return result * sign

def is_positive(x):
    return x >= 0
    
 
if __name__ == "__main__":
    print(sum(3,3))
    print(sum(5, -5))
    print(sum(3, -8))
