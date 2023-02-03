
n = int(input())
factorial = [0] * 501
factorial[0], factorial[1] = 1, 1
result = 0

for i in range(2, len(factorial)):
    factorial[i] = i*factorial[i-1]

s = str(factorial[n])
rs = s[::-1]

for x in rs:
    if x == '0':
        result += 1
    else:
        print(result)
        break
