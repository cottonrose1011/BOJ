# 소트인사이드
import sys
input = sys.stdin.readline

n = input()
array = []
for data in n:
    array.append(data)
array.sort(reverse=True)
for x in array:
    print(x, end="")
