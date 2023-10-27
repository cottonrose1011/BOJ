import sys
import math
input = sys.stdin.readline

n = int(input())
a = int(input())
array = []

for _ in range(n-1):
    num = int(input())
    array.append(num - a)
    a = num

g = array[0]
for j in range(1, len(array)):
    g = math.gcd(g, array[j])
result = 0
for each in array:
    result += each // g - 1

print(result)
