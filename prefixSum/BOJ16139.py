import sys

input = sys.stdin.readline

s = input()
q = int(input())
array = []
li = [0] * 26

for c in s:
    if 97 <= ord(c) <= 122:
        li[ord(c) - 97] += 1
        array.append(li[:])

for _ in range(q):
    a, l, r = map(str, input().split())
    result = array[int(r)][ord(a) - 97]

    if l != '0':
        result -= array[int(l) - 1][ord(a) - 97]
    print(result)
