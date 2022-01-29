import math
from utils import Utils

Mean = 500
StdD = 80
n = 100
mean = Mean 
stdDe= StdD / math.sqrt(n)
z = 1.96

a = mean - z * stdDe
b = mean + z * stdDe

print( Utils.scale (a, 2))
print( Utils.scale (b, 2))