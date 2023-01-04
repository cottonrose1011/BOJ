n = int(input())
i = 2
data = list()
while n >= 1:
    if n % i == 0:
        n = n//i
        data.append(i)
    else:
        if n == 1:
            break
        else:
            i += 1
for x in data:
    print(x)
