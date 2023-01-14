# 나이순 정렬
import sys
# input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    age, name = map(str, input().split())
    array.append((int(age), i, name))
array.sort()
for x in range(len(array)):
    print(array[x][0], array[x][2])
