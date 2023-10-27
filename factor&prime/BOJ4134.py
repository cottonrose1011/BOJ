import sys
import math


def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


input = sys.stdin.readline
n = int(input())

for _ in range(n):
    num = int(input())
    while True:
        if isPrime(num):
            print(num)
            break
        else:
            num += 1
