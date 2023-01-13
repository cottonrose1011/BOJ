# 통계학
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
array = []
count = [0] * 8001
for _ in range(n):
    num = int(input())
    array.append(num)
array.sort()
k = Counter(array).most_common()
print(int(round(sum(array)/n, 0)))
print(array[n//2])
if len(array) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(array[0])
print(array[-1] - array[0])
