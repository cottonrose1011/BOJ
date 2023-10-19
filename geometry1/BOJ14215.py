a, b, c = list(map(int, input().split()))
maxVal = max(a, b, c)
sumWithOutMaxValue = a + b + c - maxVal
while maxVal >= sumWithOutMaxValue:
    maxVal -= 1
print(sumWithOutMaxValue + maxVal)
