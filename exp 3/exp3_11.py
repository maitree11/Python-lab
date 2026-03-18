n = int(input("enter value of n: "))
series_sum = 0.0

for i in range(1, n + 1):
  series_sum += 1 / i

print("sum of series =", series_sum)
