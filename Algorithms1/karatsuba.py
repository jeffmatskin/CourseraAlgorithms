import numpy as np
import math

def karatsuba(x,y):
    if (x<10 or y <10):
        return x * y        

    n = max(len(str(x)),len(str(y)))//2
    p = 10**n

    a,b = divmod(x,p) #a = x//p, b = x%p
    c,d = divmod(y,p)    
        

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    abcd = karatsuba(a+b,c+d) - ac - bd
    return (ac*p + abcd)*p + bd
    