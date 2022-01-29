import math
from functools import reduce
import operator as op

p = 0.12
n = 10

# No more than 2 rejects

def C(n,r):
    r = min(r, n-r)
    num = reduce(op.mul, range(n, n-r,-1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return num // denom
    
result = 0
    
for i in range(0,2):
    result += C(n,i)*p**i*(1-p)**(n-i)
    
print(round(result,3))

# At least 2 rejects?
result = 0
for i in range(0,1):
    result += C(n,i)*p**i*(1-p)**(n-i)
    
print(round(1-result,3))