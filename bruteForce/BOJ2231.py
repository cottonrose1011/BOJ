n = input()
num = int(n)
array = []
hap = 0
result = 0

while num > 0:
    hap = 0
    for x in str(num):
        hap += int(x)

    if (hap + num) == int(n):
        result = num
    num -= 1

print(result)
