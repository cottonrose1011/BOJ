# 좌표 압축
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
num = set(array)  # 중복 제거

arr2 = list(num)
arr2.sort()

numValue = {}  # 값에 따른 위치 dict 형태로 기록
for i in range(len(arr2)):
    numValue[arr2[i]] = i

for i in array:
    print(numValue[i], end=" ")
