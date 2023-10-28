import math
import sys

input = sys.stdin.readline

t = int(input())
cases = [int(input()) for _ in range(t)]
n = max(cases)

array = [False, False]+[True] * (n - 1)

for i in range(2, int(math.sqrt(len(array)))+1):
    if array[i]:
        for j in range(2*i, len(array), i):
            array[j] = False

for num in cases:
    result = 0
    for i in range(2, num//2+1):
        if array[i] and array[num-i]:
            result += 1
    print(result)
