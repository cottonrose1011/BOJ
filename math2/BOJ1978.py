def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())

data = list(map(int, input().split()))
count = 0
for x in data:
    if isPrime(x):
        count += 1
print(count)
