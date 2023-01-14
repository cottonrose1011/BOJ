# 단어 정렬
import sys
# input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    s = input()
    array.append((len(s), s))
array.sort()
for x in range(len(array)):
    if x >= 1 and array[x-1][1] == array[x][1]:
        continue
    else:
        print(array[x][1])
