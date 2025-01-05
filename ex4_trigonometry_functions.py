import math

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

def sin(x,n):
    if n <= 0:
        print('n must be greater than 0 - sin')
        return 1
    for i in range(n):
        result = result + (((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1))
    return result

def cos(x,n):
    if n <= 0:
        print('n must be greater than 0 - cos')
        return 1    
    for i in range(n):
        result = result + (((-1)**i) * (x**(2*i)) / factorial(2*i))
    return result

def sinh(x,n):
    if n <= 0:
        print('n must be greater than 0 - sinh')
        return 1
    for i in range(n):
        result = result + ((x**(2*i + 1)) / factorial(2*i + 1))
    return result

def cosh(x,n):
    if n <= 0:
        print('n must be greater than 0')
        return 1
    for i in range(n):
        result = result + ((x**(2*i)) / factorial(2*i))
    return result

if __name__ == '__main__':
    x=1
    n=10
    print(sin(x,n))
    print(cos(x,n))
    print(sinh(x,n))
    print(cosh(x,n))