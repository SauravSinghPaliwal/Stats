import math

def c(x, mean, sd):
  return 0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))

max = 9800
n = 49
mean_pop = 205
sd_pop = 15

mean_sample = mean_pop * n
sd_sample = math.sqrt(n) * sd_pop

print(round(c(max, mean_sample, sd_sample), 4))