def sum(m, n):
    result = m
    increment = 1 if is_positive(n) else -1

    for i in range(0, n, increment):
        result += increment

    return result


def subtract(m, n):
    return sum(m, -n)


def multiply(m, n):
    if n == 0:
        return 0
    return divide(m, 1 / n)


def divide(m, n):
    if n == 0:
        raise ZeroDivisionError("Division by zero not allowed")

    sign = 1
    if not is_positive(m):
        sign *= -1
        m *= -1
    if not is_positive(n):
        sign *= -1
        n *= -1

    result = 0
    while m >= n and m > 0:
        result += 1
        m -= n

    return result * sign


def is_positive(x):
    return x >= 0
