#!/usr/bin/python3
import decimal
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
decimal.getcontext().prec = 400
 
if __name__ == '__main__':
    n = []
    a = []
    input() #e
    for i in range(3):
        n.append(int(input().split("=")[1].strip()))
        a.append(int(input().split("=")[1].strip()))
    A = chinese_remainder(n, a)
    N = n[0] * n[1] * n[2]
    print("A", A)
    print("N", N)
    res = int(round(decimal.Decimal(A)**(decimal.Decimal(1)/3)))
    print("MSG", res)
    print("".join([chr((res>>(i*8))&255) for i in range(1024)]))



