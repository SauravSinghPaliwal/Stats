a = int(input())
b = list(map(float,input().strip().split()))
c = list(map(float,input().strip().split()))

x = sum(b) / a
y = sum(c) / a

stdx = (sum([(i - x)**2 for i in b]) / a)**0.5
stdy = (sum([(i - y)**2 for i in c]) / a)**0.5


cov = sum([(b[i] - x) * (c[i] -y) for i in range(a)])

corr_coef = cov / (a * stdx * stdy)

print(round(corr_coef,3))
