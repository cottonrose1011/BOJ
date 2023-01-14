# 좌표 정렬하기 2
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((b, a))
array.sort()
for data in array:
    print(data[1], data[0])
