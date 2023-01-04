def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


m = int(input())
n = int(input())

primeList = list()

for i in range(m, n+1):
    if isPrime(i):
        primeList.append(i)

if len(primeList) > 0:
    primeList.sort()
    print(sum(primeList))
    print(primeList[0])
else:
    print(-1)
