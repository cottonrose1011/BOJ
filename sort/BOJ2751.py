# 수 정렬하기 2
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
for data in array:
    print(data)
