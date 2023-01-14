# 좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))
array.sort()
for data in array:
    print(data[0], data[1])
