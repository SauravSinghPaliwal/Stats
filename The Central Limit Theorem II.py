import math

def c(x, mean, sd):
  return 0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))


tickets = 250
students = 100
mean = 2.4
std = 2.0

meanS = mean * students
stds = std * math.sqrt(students)

print(round(c(tickets, meanS, stds), 4))