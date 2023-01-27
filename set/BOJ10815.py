import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
s = set(array)
m = int(input())
array2 = list(map(int, input().split()))

for x in array2:
    if x in s:
        print(1, end=" ")
    else:
        print(0, end=" ")
